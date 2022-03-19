from unicodedata import category
from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    account = models.TextField(blank=True, null=False)
    password = models.TextField(blank=True, null=False)
    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.account

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.TextField(blank=True, null=False)
    category = models.TextField(blank=True, null=False)
    name = models.TextField(blank=True, null=False)
    unitPrice = models.TextField(blank=True, null=False)
    class Meta:
        db_table = 'Product'

    def __str__(self):
        return self.id

class Other(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=False)
    unitPrice = models.TextField(blank=True, null=False)
    class Meta:
        db_table = 'Other'

    def __str__(self):
        return self.id