from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = TaggableManager()
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
