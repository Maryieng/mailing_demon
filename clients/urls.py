from django.urls import path

from clients.views import index

app_name = 'clients'
urlpatterns = [
    path('', index, name='index'),
    # path('contacts/', ProductView.as_view(), name='contacts'),
    # path('view/<int:pk>/', ProductDetailView.as_view(), name='product_info'),
]
