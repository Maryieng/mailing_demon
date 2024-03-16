from django.urls import path

from reporting.views import ReportingListView

app_name = 'reporting'

urlpatterns = [
    # path('create/', MailingsCreateView.as_view(), name='create_mailings'),
    path('list/', ReportingListView.as_view(), name='reporting_list'),
    # path('delete/<int:pk>/', MailingsDeleteView.as_view(), name='delete_mailings'),
    # path('edit/<int:pk>/', MailingsUpdateView.as_view(), name='mailings_update'),
    # path('view/<int:pk>/', MailingsDetailView.as_view(), name='view_mailings'),
]