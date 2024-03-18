from django.forms import ModelForm, DateTimeInput, Textarea
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

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
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:mailings_list')


class MailingsListView(ListView):
    """ List of all mailing settings page """
    model = Mailings

    def get_context_data(self, **kwargs):
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



class MailingsDeleteView(DeleteView):
    """ Removing mailing settings page """
    model = Mailings
    success_url = reverse_lazy('mailings:mailings_list')


class MailingsUpdateView(UpdateView):
    """ Editing mailing settings page """
    model = Mailings
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:mailings_list')


class MailingsDetailView(DetailView):
    """ Viewing your mailing settings page """
    model = Mailings
