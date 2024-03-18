from django.urls import path

from letters.views import MessageCreateView, MessageDeleteView, MessageDetailView, MessageListView, MessageUpdateView

app_name = 'letters'

urlpatterns = [
    path('create/', MessageCreateView.as_view(), name='create_letters'),
    path('list/', MessageListView.as_view(), name='letters_list'),
    path('delete/<int:pk>/', MessageDeleteView.as_view(), name='delete_letters'),
    path('edit/<int:pk>/', MessageUpdateView.as_view(), name='letters_update'),
    path('view/<int:pk>/', MessageDetailView.as_view(), name='view_letters'),
]
