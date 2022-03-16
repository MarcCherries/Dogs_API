from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    age = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=1)
