# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from farmville.sheep.models import Sheep

class Location(models.Model):
    STATUS_CHOICES=(
	(0,"Normal"),
	(1,"Panicking"),
    (2,"Dead/Non-responsive")
    )
    sheep = models.ForeignKey(Sheep, null=True, related_name="location_history")
    locId = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=False,null=True)
    pulse = models.IntegerField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    status = models.IntegerField(max_length=1, choices=STATUS_CHOICES, null=True)

    def getStatus(self):
        return self.STATUS_CHOICES[self.status][1]
    def __unicode__(self):
        return "Location for " + str(self.sheep)

