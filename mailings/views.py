from django.forms import ModelForm, DateTimeInput, Textarea
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from mailings.models import Mailings


class MailingsForm(ModelForm):     # настрока даты и времени через календарь
    class Meta:
        model = Mailings
        fields = ('name', 'start_time', 'end_time', 'frequency', 'clients', 'message')
        widgets = {
            'start_time': DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class MailingsCreateView(CreateView):   # создание рассылки
    model = Mailings
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:mailings_list')


class MailingsListView(ListView):      # страница со всеми рассылками
    model = Mailings


class MailingsDeleteView(DeleteView):      # контроллер для удаления
    model = Mailings
    success_url = reverse_lazy('mailings:mailings_list')


class MailingsUpdateView(UpdateView):    # Редактирование
    model = Mailings
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:mailings_list')


class MailingsDetailView(DetailView):      # Просмотр рассылки
    model = Mailings
