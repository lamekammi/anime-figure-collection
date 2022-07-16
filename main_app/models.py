from django.db import models
from django.urls import reverse


RATINGS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)

class Store(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stores_detail', kwargs={'pk': self.id})
        
# Create your models here.
class Figure(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    release = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=250)

    stores = models.ManyToManyField(Store)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'figure_id': self.id})

class Comment(models.Model):
    rating = models.IntegerField(
        choices=RATINGS,
        default=RATINGS[0][0]
    )
    comment = models.TextField(max_length=250)

    figure = models.ForeignKey(Figure, on_delete=models.CASCADE)

    def __str__(self):
        return f"Rating: {self.get_rating_display()} Comment: {self.comment}"

