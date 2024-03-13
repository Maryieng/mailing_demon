from django.contrib import admin

from clients.models import Clients

@admin.register(Clients)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'client_email', 'comment')
    # list_filter = ('',)
    search_fields = ('first_name', 'last_name')