from django.db import models
from django.urls import reverse

# Create your models here.
class Figure(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    release = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'figure_id': self.id})