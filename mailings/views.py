from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from mailings.forms import MailingsForm
from mailings.models import Mailings


class MailingsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """ Creating mailing settings page """
    model = Mailings
    login_url = 'users:login'
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:mailings_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

    def test_func(self):
        return not self.request.user.groups.filter(name='moderator').exists()



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


    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='moderator').exists():
            queryset = queryset
        else:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class MailingsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Removing mailing settings page """
    model = Mailings
    login_url = 'users:login'
    success_url = reverse_lazy('mailings:mailings_list')

    def test_func(self):
        return not self.request.user.groups.filter(name='moderator').exists()



class MailingsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Editing mailing settings page """
    model = Mailings
    login_url = 'users:login'
    form_class = MailingsForm
    success_url = reverse_lazy('mailings:mailings_list')

    def test_func(self):
        return not self.request.user.groups.filter(name='moderator').exists()



class MailingsDetailView(DetailView):
    """ Viewing your mailing settings page """
    model = Mailings


def toggle_activity(request, pk):
    mailing_status = get_object_or_404(Mailings, pk=pk)
    if mailing_status.is_active:
        mailing_status.is_active = False
    else:
        mailing_status.is_active = True
    mailing_status.save()

    return redirect(reverse('mailings:mailings_list'))
