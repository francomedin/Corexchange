from django.urls import path
from . import views

urlpatterns  = [
    path('', views.ContactForm.as_view(), name='contact'),
]