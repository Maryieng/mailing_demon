from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from letters.forms import MessageForm
from letters.models import Message


class MessageCreateView(CreateView):
    """ Create a message page """
    model = Message
    login_url = 'users:login'
    form_class = MessageForm
    success_url = reverse_lazy('letters:letters_list')


class MessageListView(ListView):
    """ List of all messages page """
    model = Message


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """ Delete a message page """
    model = Message
    login_url = 'users:login'
    success_url = reverse_lazy('letters:letters_list')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """ Editing a message page """
    model = Message
    login_url = 'users:login'
    form_class = MessageForm
    success_url = reverse_lazy('letters:letters_list')


class MessageDetailView(LoginRequiredMixin, DetailView):
    """ View message page """
    model = Message
    login_url = 'users:login'
