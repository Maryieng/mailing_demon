from smtplib import SMTPException

from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail

from mailings.models import Mailings
from reporting.models import Reporting

from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.core.mail import BadHeaderError, send_mail
from django.forms import ModelForm, DateTimeInput, Textarea
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from mailings.models import Mailings
from mailings.services import send_mailings


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
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        header = self.object.message.letter_subject
        body = self.object.message.body_letter
        mails = list(self.object.clients.all().values_list('client_email', flat=True))
        send_mailings(header, body, mails, self.object.name)
        return self.object

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = self.object
    #     return context

