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
    sheep.latitude = 59.5 + random.randint(-2,2)
    sheep.longitude = 8.5 + random.randint(-2,2)
    location = Location()
    location.sheep = sheep
    location.latitude = 59.5 + random.randint(-2,2)
    location.longitude = 8.5 + random.randint(-2,2)
    location.tidspunkt = datetime.now()
    location.save()
    sheep.save()
    print "Sheep moved" + sheepId
    return sheepGetList(request)
    
