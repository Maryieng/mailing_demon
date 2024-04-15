from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from letters.forms import MessageForm
from letters.models import Message


class MessageCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """ Create a message page """
    model = Message
    login_url = 'users:login'
    form_class = MessageForm
    success_url = reverse_lazy('letters:letters_list')

    def form_valid(self, form: Any) -> Any:
        """ linking the creation to the author """
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

    def test_func(self) -> Any:
        """ test function to check the user for moderation """
        return not self.request.user.groups.filter(name='moderator').exists()


class MessageListView(ListView):
    """ List of all messages page """
    model = Message

    def get_context_data(self, *args: Any, **kwargs: Any) -> Any:
        context_data = super().get_context_data(*args, **kwargs)
        context_data['message_list'] = Message.objects.all()
        return context_data

    def get_queryset(self, *args: Any, **kwargs: Any) -> Any:
        """ function to check user access rights """
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='moderator').exists():
            queryset = queryset
        else:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete a message page """
    model = Message
    login_url = 'users:login'
    success_url = reverse_lazy('letters:letters_list')

    def test_func(self) -> Any:
        """ test function to check the user for moderation """
        return not self.request.user.groups.filter(name='moderator').exists()


class MessageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Editing a message page """
    model = Message
    login_url = 'users:login'
    form_class = MessageForm
    success_url = reverse_lazy('letters:letters_list')

    def test_func(self) -> Any:
        """ test function to check the user for moderation """
        return not self.request.user.groups.filter(name='moderator').exists()


class MessageDetailView(DetailView):
    """ View message page """
    model = Message
