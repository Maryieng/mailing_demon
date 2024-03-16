from django.contrib import admin

from letters.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('letter_subject', 'body_letter')
    search_fields = ('letter_subject',)
