from django.views.generic import ListView

from reporting.models import Reporting


class ReportingListView(ListView):      # страница со всеми логами
    model = Reporting
