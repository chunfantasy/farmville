from django.db import models
from django.contrib import admin
# Create your models here.

class Sheep(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)

    def __unicode__(self):
	return None

admin.site.register(Sheep)
