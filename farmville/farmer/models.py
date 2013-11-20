from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# Create your models here.

class Farmer(AbstractUser):
    farmerId = models.CharField(max_length=7, unique = True )
    #username = models.CharField(max_length=50, null=True)
    #password = models.CharField(max_length=50, null=True)
    #first_name = models.CharField(max_length=10, null=True)
    #last_name = models.CharField(max_length=10, null=True)
    #email = models.EmailField(validators=[validate_email],max_length=50, null=True)
    tlf = models.CharField(max_length=15, null=True, blank=True)
    reserve = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.username
