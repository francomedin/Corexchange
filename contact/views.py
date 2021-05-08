from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Contacto
# Create your views here.


class ContactForm(CreateView):
    model=Contacto
    fields=['title','mail','phone','content']