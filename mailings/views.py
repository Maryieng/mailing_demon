from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import DateTimeInput, ModelForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from mailings.models import Mailings


class MailingsForm(ModelForm):
    class Meta:
        """ Filling out the date and time form via the calendar """
        model = Mailings
        fields = ('name', 'start_time', 'end_time', 'frequency', 'clients', 'message', 'status')
        widgets = {
            'start_time': DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class MailingsCreateView(CreateView):
    """ Creating mailing settings page """
    model = Mailings
    login_url = 'users:login'
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:mailings_list')


class MailingsListView(ListView):
    """ List of all mailing settings page """
    model = Mailings

    def get_context_data(self, **kwargs: Any) -> Any:
        """ Displaying the frequency of mailings in Russian """
        context = super().get_context_data(**kwargs)
        mailings = context['object_list']
        for mailing in mailings:
            if mailing.frequency == "daily":
                mailing.custom_frequency = "Раз в день"
            elif mailing.frequency == "weekly":
                mailing.custom_frequency = "Раз в неделю"
            elif mailing.frequency == "monthly":
                mailing.custom_frequency = "Раз в месяц"
        context['object_list'] = mailings
        return context


class MailingsDeleteView(LoginRequiredMixin, DeleteView):
    """ Removing mailing settings page """
    model = Mailings
    login_url = 'users:login'
    success_url = reverse_lazy('mailings:mailings_list')


class MailingsUpdateView(LoginRequiredMixin, UpdateView):
    """ Editing mailing settings page """
    model = Mailings
    login_url = 'users:login'
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:mailings_list')


class MailingsDetailView(LoginRequiredMixin, DetailView):
    """ Viewing your mailing settings page """
    model = Mailings
