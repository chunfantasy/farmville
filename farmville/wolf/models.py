from django.db import models
from django.contrib import admin
# Create your models here.
from farmville.sheep.models import Sheep
class Wolf(models.Model):
    target = models.ForeignKey(Sheep)
    time = models.DateTimeField(auto_now = True, auto_now_add = True)

    def __unicode__(self):
        return str(self.target) + " at " + str(self.time)

admin.site.register(Wolf)
