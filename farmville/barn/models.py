from django.db import models
from django.contrib import admin
# Create your models here.
from farmville.farmer.models import Farmer
class Barn(models.Model):
    STATUS_CHOICES=(
	(0,"Normal"),
	(1,"Under attack"),
    )
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(Farmer)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    status = models.IntegerField(max_length=1, choices=STATUS_CHOICES,default=0)

    def __unicode__(self):
	return self.name

admin.site.register(Barn)
