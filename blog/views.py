from django.shortcuts import render
from .models import Post
# Create your views here.

def blog(request):
    postList=Post.objects.all()
    return render(request,'blog/blog.html', {'posts':postList})
