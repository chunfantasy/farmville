from django.db import models
from django.contrib import admin
from farmville.farmer.models import Farmer
from django.core.exceptions import ValidationError


class Sheep(models.Model):
    def validate_ID_size(value):
        valSize = len(str(value))
        if valSize != 4 and valSize != 12:
            raise ValidationError(u'Ensure this value is either 4 or 12 characters (it has %s).' % valSize)

    def validate_ID_unique(value):
        print("wat: ",value)
        s = Sheep.objects.filter(farmer = Farmer)
        for sheep in s:
            print sheep.id + " vs " + value
            if sheep.id == value:
                raise ValidationError(u'%s is not a unique ID' % value)

    def validate_weight(value):
        if value > 80 or value < 0:
            raise ValidationError(u'%s is not a valid weight. Weights between 0 and 80 (kg) are accepted.' % value)

    def validate_lat(value):
        if value > 71:
            raise ValidationError(u'%s is not a valid longitude, it is too far north. (70 is max)' % value)
        if value < 58:
            raise ValidationError(u'%s is not a valid longitude, it is too far south. (58 is min)' % value)

    def validate_long(value):
        if value > 31:
            raise ValidationError(u'%s is not a valid latitude, it is too far east. (31 is max)' % value)
        if value < 5:
            raise ValidationError(u'%s is not a valid longitude, it is too far west. (5 is min)' % value)

    def validate_birthday(date):
        print 'date'

    STATUS_CHOICES=(
	(0,"Normal"),
	(1,"Panicking"),
    (2,"Dead/Non-responsive")
    )
    name = models.CharField(max_length=20, null=True)
    birthday = models.DateField(validators=[validate_birthday],auto_now_add=False,null=True)
    birthplace = models.CharField(max_length=15, null=True)
    farmer = models.ForeignKey(Farmer, null=True)
    sheepId = models.CharField(validators=[validate_ID_size, validate_ID_unique],max_length=12)
    weight = models.FloatField(validators=[validate_weight],null=True, blank=True)
    status = models.IntegerField(max_length=1, choices=STATUS_CHOICES,default=0, null=True)
    latitude = models.FloatField(validators=[validate_lat],blank=True, null=True)
    longitude = models.FloatField(validators=[validate_long],blank=True, null=True)


    def getStatus(self):
        return self.STATUS_CHOICES[self.status][1]

    def __unicode__(self):
        return str(self.farmer) + " " + str(self.name)

