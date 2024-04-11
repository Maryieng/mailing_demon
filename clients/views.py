from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from clients.forms import ClientsForm
from clients.models import Clients


class ClientsView(TemplateView):
    """ Introductory page """
    template_name = 'clients/home.html'


class ClientsCreateView(LoginRequiredMixin, CreateView):
    """ Creating clients page """
    model = Clients
    login_url = 'users:login'
    form_class = ClientsForm
    success_url = reverse_lazy('clients:clients_list')


class ClientsUpdateView(LoginRequiredMixin, UpdateView):
    """ Editing a customer card page """
    model = Clients
    login_url = 'users:login'
    form_class = ClientsForm
    success_url = reverse_lazy('clients:clients_list')


class ClientsListView(ListView):
    """ List of clients page """
    model = Clients


class ClientsDeleteView(LoginRequiredMixin, DeleteView):
    """ Deleting a customer card page """
    model = Clients
    login_url = 'users:login'
    success_url = reverse_lazy('clients:clients_list')


class StudentsDetailView(DetailView):
    """ Card for each client page """
    model = Clients
