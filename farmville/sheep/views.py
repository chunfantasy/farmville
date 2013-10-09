# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from farmville.sheep.models import Sheep
def generateSheep(request):
    s = Sheep.objects.all()
    s.delete()
    sheepList = []
    for i in range(200):
	sheep = Sheep()
	sheep.name = str(i)
	sheep.save()
	print sheep
	sheepList.append(sheep)
    return render_to_response('sheep/sheep.html',
	{'sheepList': sheepList},
	context_instance=RequestContext(request)
    )

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
