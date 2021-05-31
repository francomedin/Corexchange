from django.db import models

# Create your models here.


class Criptocoin(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
