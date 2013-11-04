# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from farmville.sheep.models import Sheep

class Location(models.Model):
    sheep = models.ForeignKey(Sheep, null=True, related_name="location_history")
    latitude = models.FloatField()
    longitude = models.FloatField()
    tidspunkt = models.DateTimeField(auto_now_add=True,null=True)

    def __unicode__(self):
        return "Location for " + str(self.sheep)

admin.site.register(Location)
