

# Create your views here.
from django.views.generic.edit import CreateView
from .models import Solicitud


class SolicitudForm(CreateView):
    model=