from django.forms import ModelForm, DateTimeInput, Textarea
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from mailings.models import Mailings


class MailingsForm(ModelForm):     # настрока даты и времени через календарь
    class Meta:
        model = Mailings
        fields = ('name', 'start_time', 'end_time', 'frequency', 'clients', 'message', 'status')
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

    def get_context_data(self, **kwargs):
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



class MailingsDeleteView(DeleteView):      # контроллер для удаления
    model = Mailings
    success_url = reverse_lazy('mailings:mailings_list')


class MailingsUpdateView(UpdateView):    # Редактирование
    model = Mailings
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:mailings_list')


class MailingsDetailView(DetailView):      # Просмотр рассылки
    model = Mailings
