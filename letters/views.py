from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from letters.models import Message


class MessageCreateView(CreateView):   # создание
    model = Message
    fields = ('letter_subject', 'body_letter')
    success_url = reverse_lazy('letters:letters_list')


class MessageListView(ListView):      # страница со всеми сообщениями
    model = Message


class MessageDeleteView(DeleteView):      # удаления
    model = Message
    success_url = reverse_lazy('letters:letters_list')


class MessageUpdateView(UpdateView):    # Редактирование
    model = Message
    fields = ('letter_subject', 'body_letter')
    success_url = reverse_lazy('letters:letters_list')


class MessageDetailView(DetailView):      # Просмотр
    model = Message


