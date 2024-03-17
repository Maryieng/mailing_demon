from django.urls import path

from reporting.views import ReportingListView

app_name = 'reporting'

urlpatterns = [
    path('list/', ReportingListView.as_view(), name='reporting_list')
]
