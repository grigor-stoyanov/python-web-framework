from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(validators=(MinValueValidator(0.01),))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
