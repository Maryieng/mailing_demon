from django.contrib import admin

from clients.models import Clients

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'client_email', 'comment')
    search_fields = ('name',)
