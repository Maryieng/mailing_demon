import random
import string
from typing import Any

from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, FormView, ListView, UpdateView

from config import settings
from users.forms import UserPasswordRecoveryForm, UserProfileForm, UserRegisterForm
from users.models import User


def generate_random_password() -> Any:
    """ random password generation """
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


class RegisterView(CreateView):
    """ User registration """
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form: Any) -> Any:
        """ registration confirmation via email and generating a secret token """
        new_user = form.save()
        new_user.is_active = False
        secret_token = ''.join([str(random.randint(0, 9)) for string in range(10)])
        new_user.token = secret_token
        message = (f'Для подтверждения вашего Е-mail перейдите по ссылке'
                   f' http://127.0.0.1:8000/users/verify/?token={secret_token}')
        send_mail(
            subject='Подтверждение регистрации',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


def activate_user(request: Any) -> Any:
    """ user activation """
    key = request.GET.get('token')
    current_user = User.objects.filter(is_active=False)
    for user in current_user:
        if str(user.token) == str(key):
            user.is_active = True
            user.token = None
            user.save()
    response = redirect(reverse_lazy('users:login'))
    return response


class UserPasswordRecoveryView(FormView):
    """ reset password and create a new one """
    template_name = 'users/user_recovery_password.html'
    form_class = UserPasswordRecoveryForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form: Any) -> Any:
        email = form.cleaned_data.get('email')
        user = User.objects.filter(email=email).first()
        random_password = generate_random_password()
        user.password = make_password(random_password)
        user.save()
        send_mail(
            'Запрос на восстановление пароля',
            f'Ваш новый пароль: {random_password}',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
        return super().form_valid(form)


class ProfileView(UpdateView):
    """ user profile """
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None) -> Any:
        """ checking access rights """
        return self.request.user


class ManagerListView(UserPassesTestMixin, ListView):
    """ moderator page """
    model = User
    template_name = 'users/manager.html'

    def test_func(self) -> Any:
        """ checking the user for moderator or superuser """
        return self.request.user.is_superuser or self.request.user.groups.filter(name='moderator').exists()


def toggle_activity(request: Any, pk: Any) -> Any:
    """ activation/deactivation """
    user_activity = get_object_or_404(User, pk=pk)
    if user_activity.is_active:
        user_activity.is_active = False
    else:
        user_activity.is_active = True
    user_activity.save()

    return redirect(reverse('users:manager_list'))
