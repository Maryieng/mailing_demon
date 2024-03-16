from django.contrib import admin

from reporting.models import Reporting


@admin.register(Reporting)
class ReportingAdmin(admin.ModelAdmin):
    list_display = ('time_log', 'status', 'response', 'mailings')
    search_fields = ('status', 'mailings',)
