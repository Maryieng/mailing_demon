from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from clients.forms import ClientsForm
from clients.models import Clients


class ClientsView(TemplateView):
    """ Introductory page """
    template_name = 'clients/home.html'


class ClientsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """ Creating clients page """
    model = Clients
    login_url = 'users:login'
    form_class = ClientsForm
    success_url = reverse_lazy('clients:clients_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

    def test_func(self):
        return not self.request.user.groups.filter(name='moderator').exists()



class ClientsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Editing a customer card page """
    model = Clients
    login_url = 'users:login'
    form_class = ClientsForm
    success_url = reverse_lazy('clients:clients_list')

    def test_func(self):
        return not self.request.user.groups.filter(name='moderator').exists()



class ClientsListView(ListView):
    """ List of clients page """
    model = Clients

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['clients_list'] = Clients.objects.all()
        return context_data

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='moderator').exists():
            queryset = queryset
        else:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class ClientsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Deleting a customer card page """
    model = Clients
    login_url = 'users:login'
    success_url = reverse_lazy('clients:clients_list')

    def test_func(self):
        return not self.request.user.groups.filter(name='moderator').exists()



class ClientsDetailView(DetailView):
    """ Card for each client page """
    model = Clients
