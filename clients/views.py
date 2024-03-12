from django.shortcuts import render
from django.views.generic import ListView

from clients.models import Clients

app_name = 'clients'

def index(request):
    return render(request, 'clients/home.html')
