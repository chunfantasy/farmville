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
    wolf = Wolf()
    wolf.target = sheep
    sheep.save()
    wolf.save()

    subject = "Sheep under attack"
    warning = "Your sheep " + sheep.sheepId + " " + sheep.name + " is under attack at " + str(wolf.time)[0:19]
    broadcaster = 'Farmville Administration'
    receiver = []
    receiver.append(farmer.email)
    if farmer.reserve:
        receiver.append(farmer.reserve.email)
    if receiver and broadcaster and warning:
        try:
            message = Message()
            message.warning = warning
            message.receiver_reserve = farmer.reserve
            message.receiver = farmer
            message.save()
            send_mail(subject, warning, broadcaster, receiver)
            print str(wolf.time)[0:19] + " Wolf " + str(wolf.id) + " is attacking"
            print str(wolf.time)[0:19] + " Sheep " + sheep.sheepId + " is under attack"
            print str(message.time)[0:19] + " Warning!! " + message.warning
        except BadHeaderError:
            return "Invalid header found"
        return HttpResponseRedirect('/')
    else:
        return "make sure all fields are valid!"
