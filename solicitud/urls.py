from django.urls import path
from . import views

urlpatterns  = [
    path('', views.SolicitudForml.as_view(), name='solicitud'),
]