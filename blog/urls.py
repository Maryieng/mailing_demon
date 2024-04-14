from django.urls import path
from django.views.decorators.cache import cache_page

import blog
from blog.views import BlogDetailView, BlogListView

app_name = 'blog'

urlpatterns = [
    path("", BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', cache_page(60)(BlogDetailView.as_view()), name='view'),
]
