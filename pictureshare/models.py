from django.db import models

# Create your models here.

class Image(models.Model):
    Image=models.ImageField(upload_to='')
    name = models.CharField(max_length=70)
    description = models.TextField()
    author = models.CharField(max_length=50, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    # category = models.ForeignKey(Category)
    # location = models.ForeignKey(Location)



class Category(models.Model):
    location = models


class Location(models.Model):
    location = models