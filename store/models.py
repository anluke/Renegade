from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    A category model for store products
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    A product model for site store
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    preorder_item = models.BooleanField(default=False, null=True, blank=False)
    description = models.TextField(default=False)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
