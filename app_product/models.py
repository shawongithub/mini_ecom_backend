from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    detail = models.TextField()
    image = models.TextField(blank=True)

    def __str__(self):
        return self.name