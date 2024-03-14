from django.urls import path

from mailings.views import MailingsCreateView, MailingsListView, MailingsDeleteView, MailingsUpdateView

app_name = 'mailings'

urlpatterns = [
    path('create/', MailingsCreateView.as_view(), name='create_mailings'),
    path('list/', MailingsListView.as_view(), name='mailings_list'),
    path('delete/<int:pk>/', MailingsDeleteView.as_view(), name='delete_mailings'),
    path('edit/<int:pk>/', MailingsUpdateView.as_view(), name='mailings_update'),
]
