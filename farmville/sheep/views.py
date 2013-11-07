# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
from farmville.farmer.models import Farmer
from farmville.sheep.models import Sheep
from farmville.location.models import Location
from django.contrib.auth.models import AbstractUser
import random
import string
from django.core.mail import send_mail, BadHeaderError
common_names = ['Anne','Inger','Kari','Marit','Ingrid','Liv','Eva','Berit','Astrid',
                'Bjorg','Hilde','Anna','Solveig','Marianne','Randi','Ida','Nina',
                'Maria','Elisabeth','Kristin','Bente','Heidi','Silje','Hanne',
                'Jan','Per','Bjorn','Ole','Lars','Kjell','Knut','Arne','Svein',
                'Thomas','Hans','Geir','Tor','Morten','Terje','Odd','Erik','Martin',
                'Andreas','John','Anders','Rune','Trond','Tore','Daniel','Jon']
               
def sendMail(request):
    subject = "Sau under angrep"
    message = "test"
    broadcaster = "sondre.erstad@gmail.com"
    receiver = ['sondre_erstad@hotmail.com']
    if receiver and broadcaster and message:
        try:
            send_mail(subject,message, broadcaster, receiver)
        except BadHeaderError:
            return "Invalid header found"
        return HttpResponseRedirect('/farmer/farmerLogin')
    else:
        return "make sure all fields are valid!"

def sheepGenerateTest(request):
    names = common_names[::]
    farmer = request.user
    s = Sheep.objects.filter(farmer = farmer)
    s.delete()
    sheepList = []
    for i in range(50):
        sheep = Sheep()
        sheep.Farmer = farmer
        sheep.name = names.pop(random.randint(0,50-i-1))
        sheep.birthday = date.today()
        sheep.sheepId = farmer.farmerId + str(sheep.birthday)[3] + str(i+1).zfill(4)
        sheep.birthplace = sheep.name + "stad"
        sheep.status = random.randint(0,3)
        sheep.latitude = 59.5 + random.random()
        sheep.longitude = 8.5 + random.random()
        sheep.save()
        print(sheep.name,sheep.birthday,sheep.sheepId)
        sheepList.append(sheep)
    return render_to_response('sheep/sheep.html',
	{'sheepList': sheepList},
	context_instance=RequestContext(request)
    )

def sheepGenerate(request):
    names = common_names[::]
    farmer = request.user
    try:
        quantity = int(request.POST['quantity'])
    except:
        quantity = 0

    s = Sheep.objects.filter(farmer = farmer)
    sheepList = []
    for sheep in s:
        sheepList.append(sheep)
    if sheepList:
        lastid = int(sheepList[-1].sheepId[8:12])
    else:
        lastid = 0
    for i in range(quantity):
        sheep = Sheep()
        sheep.farmer = farmer
        sheep.name = names[random.randint(0,49)]
        sheep.birthday = date.today()
        sheep.sheepId = farmer.farmerId + str(sheep.birthday)[3] + str(lastid + 1 + i).zfill(4)
        sheep.birthplace = sheep.name + "stad"
        sheep.status = random.randint(0,3)
        sheep.latitude = 59.5 + random.random()
        sheep.longitude = 8.5 + random.random()

        location = Location()
        location.latitude = sheep.latitude
        location.longitude = sheep.longitude
        location.sheep = sheep
        location.save()
        sheep.save()
		
        print(sheep.name,sheep.birthday,sheep.sheepId)
        sheepList.append(sheep)
	
    return render_to_response('sheep/sheepList.html',
	    {'sheepList': sheepList},
	    context_instance=RequestContext(request)
        )

def sheepGetList(request):
    farmer = request.user
    sheepList = Sheep.objects.filter(farmer = farmer)
    return render_to_response('sheep/logg.html',
	{'sheepList': sheepList},
	context_instance=RequestContext(request)
    )
    
def getMultipleSheep(request):
    farmer = request.user
    s = Sheep.objects.filter(farmer = farmer)
    sheepList = []
    if len(request.POST["id"]) == 5:
        id = farmer.farmerId + request.POST["id"]
    elif len(request.POST["id"]) == 12:
        id = request.POST["id"]
    for sheep in s:
        if sheep.sheepId == id:
            sheepList.append(sheep)
    return render_to_response('sheep/logg.html',
    {'sheepList':sheepList},
    context_instance=RequestContext(request))

def getSheep(request):
    result = Sheep()
    farmer = request.user
    s = Sheep.objects.filter(farmer = farmer)
    sheepList = []
    if len(request.POST["id"]) == 5:
        id = farmer.farmerId + request.POST["id"]
    elif len(request.POST["id"]) == 12:
        id = request.POST["id"]
    for sheep in s:
        if sheep.sheepId == id:
            result = sheep
    return render_to_response('sheep/sheep_detail.html',
    {'sheepList':result},
    context_instance=RequestContext(request))

def sheepRegister(request):
    farmer = request.user
    s = Sheep.objects.filter(farmer = farmer)
    print(s)
    sheepList = []
    for sheep in s:
        sheepList.append(sheep)
    if sheepList:
        sheepList[-1].sheepId[8:12]
        lastid = int(sheepList[-1].sheepId[8:12])
    else:
        lastid = 0
    tempid = request.POST["lastid"]
    
    try:
        if len(tempid) == 4:
            print tempid
            print lastid
            if int(tempid) > lastid:
                lastid = int(tempid) - 1
            else:
                raise
        else:
            raise

        sheep = Sheep()
        sheep.farmer = farmer
        sheep.name = request.POST["name"]
        sheep.birthday = request.POST["birthday"]
        sheep.sheepId = farmer.farmerId + str(sheep.birthday)[3] + str(lastid + 1).zfill(4)
        sheep.birthplace = request.POST["birthplace"]
        sheep.status = random.randint(0,3)
        sheep.latitude = 59.5 + random.randint(-2,2)
        sheep.longitude = 8.5 + random.randint(-2,2)
        sheep.save()
        print(sheep.name,sheep.birthday,sheep.sheepId)
        sheepList.append(sheep)
    except:
        result = "Please fill with correct information"
        return render_to_response('farmer/farmer_result_sheepRegister.html',
	    {'farmer': farmer,
	    'result': result},
	    context_instance=RequestContext(request)
	    )
    return render_to_response('sheep/sheep.html',
	{'sheepList': sheepList},
	context_instance=RequestContext(request)
    )

def sheepDelete(request):
    farmer = request.user
    sheepList = Sheep.objects.all()
    sheepList.delete()
    return render_to_response('sheep/sheep.html',
	{'sheepList': sheepList},
	context_instance=RequestContext(request)
    )

