from django.db import models

# Create your models here.

class SocialNetwork(models.Model):
    name=models.CharField(max_length=30)
    url=models.URLField(blank=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
