from django.shortcuts import render
from contact.models import Contacto
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


def home(request):
    return render(request, "core/home.html")








