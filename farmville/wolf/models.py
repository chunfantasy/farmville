from django.db import models
from django.contrib import admin
# Create your models here.
from farmville.sheep.models import Sheep
class Wolf(models.Model):
    target = models.ForeignKey(Sheep)
    time = models.TimeField()

    def __unicode__(self):
	return self.target + " at " + self.time

admin.site.register(Wolf)
