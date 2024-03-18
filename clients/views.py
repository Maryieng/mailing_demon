from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, TemplateView, DeleteView, DetailView

from clients.models import Clients


class ClientsView(TemplateView):
    """ Introductory page """
    template_name = 'clients/home.html'


class ClientsCreateView(CreateView):
    """ Creating clients page """
    model = Clients
    fields = ('name', 'client_email')
    success_url = reverse_lazy('clients:clients_list')


class ClientsUpdateView(UpdateView):
    """ Editing a customer card page """
    model = Clients
    fields = ('name', 'client_email')
    success_url = reverse_lazy('clients:clients_list')


class ClientsListView(ListView):
    """ List of clients page """
    model = Clients


class ClientsDeleteView(DeleteView):
    """ Deleting a customer card page """
    model = Clients
    success_url = reverse_lazy('clients:clients_list')


class StudentsDetailView(DetailView):
    """ Card for each client page """
    model = Clients
