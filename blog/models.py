from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=30)
    url=models.URLField()
    content=models.TextField()
    image=models.ImageField()
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    #Author=


    def __str__(self):
        return self.title

