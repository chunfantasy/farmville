# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from farmville.farmer.models import Farmer
from farmville.sheep.models import Sheep
from django.contrib.auth.models import AbstractUser


def generateSheep(request):
    farmer = request.user
    #farmer = farmer[len(farmer)-1]
    s = Sheep.objects.all()\
        #.get(Farmer = farmer)
    s.delete()
    sheepList = []
    for i in range(50):
        sheep = Sheep()
        sheep.Farmer = farmer
        sheep.name = str(i)
        sheep.birthday = "2013-01-01"
        print(farmer.farmerid)
        sheep.sheepID = farmer.farmerid+sheep.birthday[2:4]+str(sheep.nr)
        sheep.save()
        print(sheep.name,sheep.birthday,sheep.sheepID)
        sheepList.append(sheep)
    return render_to_response('sheep/sheep.html',
	{'sheepList': sheepList},
	context_instance=RequestContext(request)
    )
"""
def sheepRegister(request):
    farmer = request.farmer
    sheep = Sheep()
    s = Sheep.objects.filter(farmer=farmer, date=thisyear)
    if s == None:
	    sheep.id = farmer.id + thisyear + "000"
    else:
	    sheep.id = farmer.id + thisyear + (s.id+1)
    return render_to_response('sheep/sheep.html',
	{'sheepList': sheepList},
	context_instance=RequestContext(request)
    )
"""