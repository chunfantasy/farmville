# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from farmville.sheep.models import Sheep
from farmville.farmer.models import Farmer
from farmville.wolf.models import Wolf
from farmville.message.models import Message

from django.core.mail import send_mail, BadHeaderError

import random

def wolfAttackRandomSheep(request):
    sheepList = Sheep.objects.all()
    l = len(sheepList)
    sheep = sheepList[random.randint(0, l-1)]
    sheep.status = 1
    farmer = Farmer.objects.get(username = sheep.farmer.username)
    admin = Farmer.objects.get(username = 'a')
    wolf = Wolf()
    wolf.target = sheep

    subject = "Sau under angrep"
    warning = "test"
    broadcaster = admin.username
    receiver = [farmer.username]
    if receiver and broadcaster and warning:
        try:
            #send_mail(subject,message, broadcaster, receiver)
         message = Message()
         message.warning = warning
         message.sender = admin
         message.receiver = farmer
         sheep.save()
         wolf.save()
         message.save()
         print str(wolf.time)[0:19] + " Wolf " + str(wolf.id) + " is attacking"
         print str(wolf.time)[0:19] + " Sheep " + sheep.sheepId + " is under attack"
         print str(message.time)[0:19] + " Message: " + message.warning
        except BadHeaderError:
            return "Invalid header found"
        return HttpResponseRedirect('/farmer/farmerLogin')
    else:
        return "make sure all fields are valid!"
