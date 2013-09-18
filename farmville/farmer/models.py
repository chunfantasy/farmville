from django.db import models
from django.contrib.admin

# Create your models here.
class Farmer(models.Model):
    name = CharField(max_length=50)
    email = CharField(max_length=100)
