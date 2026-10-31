from django.db import models

# Create your models here.


class user(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField(max_length=3)

class dev(models.Model):
    name = models.CharField(max_length=100)

