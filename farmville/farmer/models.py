from django.db import models
from django.contrib.admin

# Create your models here.
class Farmer(models.Model):
    name = CharField(max_length=50)
    phone_number = IntField(max_length = 8) #### is IntField correct???
    email = CharField(max_length=100)
    
