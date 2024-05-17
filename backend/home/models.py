from django.conf import settings
from django.db import models


class Product(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    price = models.IntegerField()


class Solid(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    price = models.IntegerField()


class Liquid(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    price = models.IntegerField()


class French(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    price = models.IntegerField()


class Spanish(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    price = models.IntegerField()


class Rdsc(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    price = models.IntegerField()
