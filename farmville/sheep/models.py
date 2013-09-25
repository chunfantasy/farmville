from django.db import models
from django.contrib import admin
# Create your models here.
from farmville.barn.models import Barn
class Sheep(models.Model):
    STATUS_CHOICES=(
	(0,"Normal"),
	(1,"Under attack"),
    )

    name = models.CharField(max_length=20, null=True)
    birthday = models.DateField(null=True)
    birthplace = models.CharField(max_length=15, null=True)
    barn = models.ForeignKey(Barn, null=True)
    weight = models.FloatField(null=True)
    status = models.IntegerField(max_length=1, choices=STATUS_CHOICES,default=0, null=True)

    def __unicode__(self):
	return str(self.barn) + " " + str(self.name)
 
admin.site.register(Sheep)
