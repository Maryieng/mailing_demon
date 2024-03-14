from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from mailings.models import Mailings


class MailingsCreateView(CreateView):     # Создание
    model = Mailings
    fields = ('name', 'start_time', 'end_time', 'frequency', 'clients')
    success_url = reverse_lazy('mailings:mailings_list')


class MailingsListView(ListView):      # страница со всеми клиентами
    model = Mailings


class MailingsDeleteView(DeleteView):      # контроллер для удаления
    model = Mailings
    success_url = reverse_lazy('mailings:mailings_list')


class MailingsUpdateView(UpdateView):    # Редактирование
    model = Mailings
    fields = ('name', 'start_time', 'end_time', 'frequency', 'clients')
    success_url = reverse_lazy('mailings:mailings_list')
