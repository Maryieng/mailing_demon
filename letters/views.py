from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from letters.models import Message


class MessageCreateView(CreateView):
    """ Create a message page """
    model = Message
    fields = ('letter_subject', 'body_letter')
    success_url = reverse_lazy('letters:letters_list')


class MessageListView(ListView):
    """ List of all messages page """
    model = Message


class MessageDeleteView(DeleteView):
    """ Delete a message page """
    model = Message
    success_url = reverse_lazy('letters:letters_list')


class MessageUpdateView(UpdateView):
    """ Editing a message page """
    model = Message
    fields = ('letter_subject', 'body_letter')
    success_url = reverse_lazy('letters:letters_list')


class MessageDetailView(DetailView):
    """ View message page """
    model = Message


