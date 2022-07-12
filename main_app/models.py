from django.db import models

# Create your models here.
class Figure(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    release = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=250)