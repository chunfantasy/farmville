from django.db import models
from django.contrib import admin
from farmville.farmer.models import Farmer

class Sheep(models.Model):
    STATUS_CHOICES=(
	(0,"Normal"),
	(1,"Under attack"),
    (2,"Dead/Non-responsive")
    )
    name = models.CharField(max_length=20, null=True)
    birthday = models.DateField(auto_now_add=True,null=True)
    birthplace = models.CharField(max_length=15, null=True)
    farmer = models.ForeignKey(Farmer, null=True)
    sheepId = models.CharField(max_length=12)
    weight = models.FloatField(null=True)
    status = models.IntegerField(max_length=1, choices=STATUS_CHOICES,default=0, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __unicode__(self):
        return str(self.farmer) + " " + str(self.name)

admin.site.register(Sheep)
