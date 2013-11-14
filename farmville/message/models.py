# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from farmville.farmer.models import Farmer
# Create your models here.

class Message(models.Model):
    warning = models.CharField(max_length=500, null=True, blank=True)
    receiver_reserve = models.ForeignKey(Farmer, related_name="receiver_reserve", null=True, blank=True)
    receiver = models.ForeignKey(Farmer, related_name="receiver", null=True, blank=True)
    time = models.DateTimeField(auto_now = True, auto_now_add = True)

    def __unicode__(self):
        return "Message" + str(self.id)

