from django.db import models

# Create your models here.

class Products(models.Model):
    description = models.CharField(max_length = 200)
    price = models.IntegerField()
