from typing import Any

from django.views.generic import ListView

from reporting.models import Reporting


class ReportingListView(ListView):
    """ Page with all logs """
    model = Reporting

    def get_context_data(self, **kwargs: Any) -> Any:
        """ Status display in Russian """
        context = super().get_context_data(**kwargs)
        for obj in context['object_list']:
            obj.status_display = 'Успешно' if obj.status else 'Неуспешно'
        return context
