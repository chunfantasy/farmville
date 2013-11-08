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
    sheep.latitude = 59.5 + random.random()
    sheep.longitude = 8.5 + random.random()
    location = Location()
    location.sheep = sheep
    location.latitude = 59.5 + random.random()
    location.longitude = 8.5 + random.random()
    location.tidspunkt = datetime.now()
    location.save()
    sheep.save()
    print "Sheep moved " + sheepId
    return sheepGetList(request)
    
def locationMoveAll(request):
    sheepList = Sheep.objects.all()
    for sheep in sheepList:
        sheep.latitude = 59.5 + random.random()
        sheep.longitude = 8.5 + random.random()
        location = Location()
        location.sheep = sheep
        location.latitude = 59.5 + random.random()
        location.longitude = 8.5 + random.random()
        location.tidspunkt = datetime(2013, 11, 11, random.randint(0, 23), 0, 0)
        location.save()
        sheep.save()
        print "Sheep moved " + sheep.sheepId
    return sheepGetList(request)
