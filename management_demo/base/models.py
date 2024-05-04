from django.db import models

# Create your models here.

class Product(models.Model):
    # id field default created by django
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    in_stock = models.BooleanField()
