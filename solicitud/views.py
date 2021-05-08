

# Create your views here.
from django.views.generic.edit import CreateView
from .models import Solicitud
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import login_required


@method_decorator(login_required, name='dispatch')
class SolicitudForm(CreateView):
    model = +
