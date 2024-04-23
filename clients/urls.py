from django.urls import path

from clients.views import (ClientsCreateView, ClientsDeleteView, ClientsDetailView, ClientsListView, ClientsUpdateView,
                           HomeView)

app_name = 'clients'

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('create/', ClientsCreateView.as_view(), name='create_clients'),
    path('edit/<int:pk>/', ClientsUpdateView.as_view(), name='update_clients'),
    path('list/', ClientsListView.as_view(), name='clients_list'),
    path('delete/<int:pk>/', ClientsDeleteView.as_view(), name='delete_clients'),
    path('view/<int:pk>/', ClientsDetailView.as_view(), name='view_clients'),
]
