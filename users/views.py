import random

from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView, UpdateView, ListView

from config import settings
from users.forms import UserRegisterForm, UserPasswordRecoveryForm, UserProfileForm
from users.models import User
import string


def generate_random_password():
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        new_user.is_active = False
        secret_token = ''.join([str(random.randint(0, 9)) for string in range(10)])
        new_user.token = secret_token
        message = f'Для подтверждения вашего Е-mail перейдите по ссылке http://127.0.0.1:8000/users/verify/?token={secret_token}'
        send_mail(
            subject='Подтверждение регистрации',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


def activate_user(request):
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
    template_name = 'users/user_recovery_password.html'
    form_class = UserPasswordRecoveryForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
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
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class ManagerListView(UserPassesTestMixin, ListView):
    model = User
    template_name = 'users/manager.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='moderator').exists()


def toggle_activity(request, pk):
    user_activity = get_object_or_404(User, pk=pk)
    if user_activity.is_active:
        user_activity.is_active = False
    else:
        user_activity.is_active = True
    user_activity.save()

    return redirect(reverse('users:manager_list'))
