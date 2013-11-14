# -*- coding: utf-8 -*-
# Create your views here.
from datetime import datetime

from farmville.sheep.views import sheepGetList
from farmville.sheep.models import Sheep
from farmville.location.models import Location

import random

def locationMove(request):
    sheepId = request.POST["sheepId"]
    sheep = Sheep.objects.get(sheepId = sheepId)
    locations = Location.objects.filter(sheep = sheep)
    location = Location()
    location.sheep = sheep
    location.latitude = sheep.latitude
    location.longitude = sheep.longitude
    location.timestamp = datetime.now()
    location.status = random.randint(0,2)
    lastId = locations[0].locId
    location.locId = lastId+1
    location.save()
    sheep.latitude = 59.5 + random.random() + (random.random()/10)
    sheep.longitude = 8.5 + random.random() + (random.random()/10)
    sheep.save()
    print "Sheep moved " + sheepId
    return sheepGetList(request)

def locationMoveAll(request):
    sheepList = Sheep.objects.all()
    for sheep in sheepList:
        locations = Location.objects.filter(sheep = sheep)
        lastId = locations[0].locId
        location = Location()
        location.sheep = sheep
        location.locId = lastId+1
        location.latitude = sheep.latitude
        location.longitude = sheep.longitude
        location.timestamp = datetime(2013, 11, 11, random.randint(0, 23), 0, 0)
        location.status = random.randint(0,2)
        location.save()
        sheep.latitude = 59.5 + random.random() + (random.random()/10)
        sheep.longitude = 8.5 + random.random() + (random.random()/10)
        sheep.save()
        print "Sheep moved " + sheep.sheepId
    return sheepGetList(request)
