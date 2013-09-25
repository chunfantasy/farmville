from django.db import models
from django.contrib import admin
# Create your models here.

class Farmer(models.Model):
    username = models.CharField(max_length=50, primary_key = True)
    password = models.CharField(max_length=50)
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    tlf = models.CharField(max_length=15)
    reserve = models.ForeignKey('self')

    def __unicode__(self):
	return self.username

admin.site.register(Farmer)
