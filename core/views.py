from django.shortcuts import render



def home(request):
    return render(request,"core/home.html")

def service(request):
    return render(request,'core/service.html')