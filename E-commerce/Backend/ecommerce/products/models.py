from django.db import models

# Create your models here.
"""
sell a product->load to module for prediction,
"""
class Product(models.Model):
    store=models.CharField(max_length=1000)
    location=models.CharField(max_length=1000)
    category=models.CharField(max_length=1000)
    price=models.FloatField()
    date=models.CharField(max_length=1000)

class Category(models.Model):
    name=models.CharField(max_length=50)

