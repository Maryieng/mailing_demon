from django.contrib import admin

from mailings.models import Mailings


@admin.register(Mailings)
class MailingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'frequency', 'status', 'message')
    search_fields = ('name', 'status',)
