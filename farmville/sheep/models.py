from django.db import models
from django.contrib import admin
# Create your models here.

class Sheep(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    birth_place = models.CharField(max_length = 100)
    birth_date = models.IntegerField(default =2013, min_length = 4)
    veigth = models.IntegerField(default = 0)

    def __unicode__(self):
	return None

admin.site.register(Sheep)
