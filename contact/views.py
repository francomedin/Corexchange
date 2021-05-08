from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Contacto
from django.urls import reverse_lazy
# Create your views here.


class ContactForm(CreateView):
    model=Contacto
    fields=['title','mail','phone','content']
    success_url = reverse_lazy('home')