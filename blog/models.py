from django.db import models


# Create your models here.


class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    url = models.URLField()
    content = models.TextField()
    image = models.ImageField(verbose_name='Imagen',
                              upload_to='blog', blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
