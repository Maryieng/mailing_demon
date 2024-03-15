from django.urls import path

from clients.views import (ClientsCreateView, ClientsUpdateView, ClientsView, ClientsListView, ClientsDeleteView,
                           StudentsDetailView)

app_name = 'clients'

urlpatterns = [
    path('', ClientsView.as_view(), name='home_page'),
    path('create/', ClientsCreateView.as_view(), name='create_clients'),
    path('edit/<int:pk>/', ClientsUpdateView.as_view(), name='update_clients'),
    path('list/', ClientsListView.as_view(), name='clients_list'),
    path('delete/<int:pk>/', ClientsDeleteView.as_view(), name='delete_clients'),
    path('view/<int:pk>/', StudentsDetailView.as_view(), name='view_clients'),
]
