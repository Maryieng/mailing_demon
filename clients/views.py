from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, TemplateView, DeleteView, DetailView

from clients.models import Clients


class ClientsView(TemplateView):       # вводная страница
    template_name = 'clients/home.html'


class ClientsCreateView(CreateView):     # Создание
    model = Clients
    fields = ('name', 'client_email')
    success_url = reverse_lazy('clients:clients_list')


class ClientsUpdateView(UpdateView):    # Редактирование
    model = Clients
    fields = ('name', 'client_email')
    success_url = reverse_lazy('clients:clients_list')


class ClientsListView(ListView):      # страница со всеми клиентами
    model = Clients


class ClientsDeleteView(DeleteView):      # контроллер для удаления
    model = Clients
    success_url = reverse_lazy('clients:clients_list')


class StudentsDetailView(DetailView):      # страница каждого клиента
    model = Clients
