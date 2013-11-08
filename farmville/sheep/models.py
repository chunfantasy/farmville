from django.db import models
from django.contrib import admin
from farmville.farmer.models import Farmer
from django.core.exceptions import ValidationError


class Sheep(models.Model):
    def validate_size(value):
        valSize = len(str(value))
        if valSize  < 5:
            #if
            raise ValidationError(u'%s is not a valid ID, an ID' % value)

    def validate_unique(value, exclude=None):
        s = Sheep.objects.filter(farmer = Farmer)
        for i in s:
            if s.id == value:
                raise ValidationError(u'%s is not a unique ID' % value)

    STATUS_CHOICES=(
	(0,"Normal"),
	(1,"Panicking"),
    (2,"Dead/Non-responsive")
    )
    name = models.CharField(max_length=20, null=True)
    birthday = models.DateField(auto_now_add=False,null=True)
    birthplace = models.CharField(max_length=15, null=True)
    farmer = models.ForeignKey(Farmer, null=True)
    sheepId = models.CharField(validators=[validate_size, validate_unique],max_length=12)
    weight = models.FloatField(null=True, blank=True)
    status = models.IntegerField(max_length=1, choices=STATUS_CHOICES,default=0, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)


    def getStatus(self):
        return self.STATUS_CHOICES[self.status-1][1]

    def __unicode__(self):
        return str(self.farmer) + " " + str(self.name)

