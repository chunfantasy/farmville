# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
from farmville.farmer.models import Farmer
from farmville.sheep.models import Sheep
from django.contrib.auth.models import AbstractUser


def sheepGenerate(request):
    farmer = request.user
    s = Sheep.objects.all()
    s.delete()
    sheepList = []
    for i in range(50):
        sheep = Sheep()
        sheep.Farmer = farmer
        sheep.name = str(i)
	sheep.birthday = date.today()
        sheep.sheepid = farmer.farmerid + str(sheep.birthday)[2:4] + str(i).zfill(3)
        sheep.save()
        print(sheep.name,sheep.birthday,sheep.sheepid)
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
