

# Create your views here.
from django.views.generic.edit import CreateView
from django.shortcuts import render
#from django.utils.decorators import method_decorator
#from django.contrib.admin.views.decorators import login_required


# @method_decorator(login_required, name='dispatch')

def solicitud(request):
    return render(request, 'solicitud/solicitud_form.html')
