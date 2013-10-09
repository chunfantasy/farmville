from django.db import models
from django.contrib import admin
# Create your models here.

class Farmer(models.Model):
    farmerid = models.CharField(max_length=7, primary_key = True)
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    firstname = models.CharField(max_length=10, null=True)
    lastname = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=50, null=True)
    tlf = models.CharField(max_length=15, null=True)
    reserve = models.ForeignKey('self', null=True)

    def __unicode__(self):
	return self.username

admin.site.register(Farmer)
