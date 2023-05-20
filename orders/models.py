from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
from products.models import Product

class Departments(models.Model):
    """ A model to create departments """
    class Meta:
        verbose_name_plural = 'Departments'

    name = models.CharField(max_length=254)
    short_name = models.CharField(max_length=254, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    """ A models for orders """

    department = models.ForeignKey('Departments', null=True, blank=True, on_delete=models.SET_NULL)
    order_number = models.CharField(max_length=32, null=False, editable=False,unique=True)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.order_number