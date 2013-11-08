from django.db import models
from django.contrib import admin
from farmville.farmer.models import Farmer
# Create your models here.

class Message(models.Model):
    warning = models.CharField(max_length=500)
    sender = models.ForeignKey(Farmer, related_name="sender")
    receiver = models.ForeignKey(Farmer, related_name="receiver")
    time = models.DateTimeField(auto_now = True, auto_now_add = True)

    def __unicode__(self):
	return "Message" + str(self.id)

admin.site.register(Message)
