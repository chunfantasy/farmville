from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Farmer(AbstractUser):
    farmerId = models.CharField(max_length=7)
    #username = models.CharField(max_length=50, null=True)
    #password = models.CharField(max_length=50, null=True)
    #first_name = models.CharField(max_length=10, null=True)
    #last_name = models.CharField(max_length=10, null=True)
    #email = models.EmailField(max_length=50, null=True)
    tlf = models.CharField(max_length=15, null=True, blank=True)
    reserve = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.username
