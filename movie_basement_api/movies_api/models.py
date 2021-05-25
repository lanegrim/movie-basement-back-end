from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=64)
    image = models.CharField(
        max_length=2048, default='https: // demofree.sirv.com/nope-not-here.jpg')
    year = models.CharField(max_length=4)
    synopsis = models.CharField(max_length=1024)
    rating = models.CharField(max_length=2)
