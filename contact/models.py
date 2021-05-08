from django.db import models

# Create your models here.

class Contacto(models.Model):
    title=models.CharField(max_length=25)
    mail=models.EmailField()
    phone=models.BigIntegerField()
    content=models.TextField()
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    def __str__(self):
        return self.title