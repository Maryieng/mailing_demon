from django.views.generic import ListView

from reporting.models import Reporting


class ReportingListView(ListView):      # страница со всеми логами
    model = Reporting

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for obj in context['object_list']:
            obj.status_display = 'Успешно' if obj.status else 'Неуспешно'
        return context
