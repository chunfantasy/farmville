# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,user_passes_test
from farmville.farmer.models import Farmer
from farmville.sheep.models import Sheep
from farmville.location.models import Location
from datetime import datetime
from datetime import timedelta
import random

common_names = ['Anne','Inger','Kari','Marit','Ingrid','Liv','Eva','Berit','Astrid',
                'Bjorg','Hilde','Anna','Solveig','Marianne','Randi','Ida','Nina',
                'Maria','Elisabeth','Kristin','Bente','Heidi','Silje','Hanne',
                'Jan','Per','Bjorn','Ole','Lars','Kjell','Knut','Arne','Svein',
                'Thomas','Hans','Geir','Tor','Morten','Terje','Odd','Erik','Martin',
                'Andreas','John','Anders','Rune','Trond','Tore','Daniel','Jon']

def index(request):
    if request.user.is_authenticated():
            return HttpResponseRedirect('/farmer/farmer')
    return render_to_response('index.html',
    {},
    context_instance=RequestContext(request))


@user_passes_test(lambda user: user.is_superuser)
def initiate(request):
    names = common_names[::]
    farmerlist = Farmer.objects.all()
    if len(farmerlist) <= 2:
        for i in range(len(farmerlist)):
            f = farmerlist[i]
            f.farmerId = str(i+1).zfill(7)
            f.save()
    lastid = len(farmerlist)
    print "initiating...", i
    for i in range(5):
        name = common_names[i]
        username = name.lower() + "@farmville.com"
        password = "1"
        farmer = Farmer.objects.create_user(username = username, password = password)
        farmer.first_name = name
        farmer.last_name = name
        farmer.farmerId = str(int(lastid) + int(i) + 1).zfill(7)
        farmer.email = username
        farmer.reserve = farmerlist[0]
        farmer.is_staff = True
        farmer.user_permissions.add(20) #change user
        farmer.user_permissions.add(22) #add sheep
        farmer.user_permissions.add(23) #change sheep
        farmer.user_permissions.add(24) #delete sheep
        farmer.user_permissions.add(33) #delete location
        farmer.user_permissions.add(26) #change message
        farmer.save()
        for j in range(5):
            sheep = Sheep()
            sheep.farmer = farmer
            sheep.name = names[random.randint(0,49)]
            sheep.birthday = datetime(random.randint(2008,2013),random.randint(1,11),random.randint(1,11))
            sheep.sheepId = farmer.farmerId.zfill(7) + str(sheep.birthday)[3] + str(lastid+j).zfill(4)
            sheep.birthplace = sheep.name + "stad"
            sheep.status = 0
            sheep.latitude = 59.5 + random.random()
            sheep.longitude = 8.5 + random.random()
            sheep.save()
            timestamp = datetime(2013,11,20,12,0,0,0)
            latitude = sheep.latitude
            longitude = sheep.longitude
            for k in range(5):
                location = Location()
                location.locId = k
                location.latitude = latitude + random.random()/20*float(random.randint(-2,2))
                location.longitude = longitude + random.random()/20*float(random.randint(-2,2))
                location.sheep = sheep
                location.timestamp = timestamp
                location.temperature = (float(random.randint(384,400)))/10
                location.pulse = random.randint(60,90)
                location.status = random.randint(0,1)
                location.save()
                longitude = location.longitude
                latitude = location.latitude
                timestamp = timestamp - timedelta(hours = 8)


    return render_to_response('index.html',
    {},
    context_instance=RequestContext(request))

@login_required
def initiate2(request):
    names = common_names[::]
    farmerlist = Farmer.objects.all()
    if len(farmerlist) <= 2:
        for i in range(len(farmerlist)):
            f = farmerlist[i]
            f.farmerId = str(i+1).zfill(7)
            f.save()
    lastid = len(farmerlist)
    for i in range(200):
        name = common_names[i]
        username = str(i) + "@farmville.com"
        password = "1"
        farmer = Farmer.objects.create_user(username = username, password = password)
        farmer.first_name = str(i)
        farmer.last_name = str(i)
        farmer.farmerId = str(int(lastid) + int(i) + 1).zfill(7)
        farmer.email = username
        farmer.reserve = farmerlist[0]
        farmer.is_staff = True
        farmer.user_permissions.add(20) #change user
        farmer.user_permissions.add(22) #add sheep
        farmer.user_permissions.add(23) #change sheep
        farmer.user_permissions.add(24) #delete sheep
        farmer.user_permissions.add(33) #delete location
        farmer.user_permissions.add(26) #change message
        farmer.save()
        for j in range(5):
            sheep = Sheep()
            sheep.farmer = farmer
            sheep.name = names[random.randint(0,49)]
            sheep.birthday = datetime(random.randint(2008,2013),random.randint(1,11),random.randint(1,11))
            sheep.sheepId = farmer.farmerId.zfill(7) + str(sheep.birthday)[3] + str(lastid+j).zfill(4)
            sheep.birthplace = sheep.name + "stad"
            sheep.status = 2
            sheep.latitude = 59.5 + random.random()
            sheep.longitude = 8.5 + random.random()
            sheep.save()
            dag = datetime(2013,11,20,12,0,0,0)
            longitude = sheep.longitude
            latitude = sheep.latitude
            for k in range(5):
                location = Location()
                location.latitude = latitude + random.random()/2*(float(random.randint(-1,1)))
                location.longitude = longitude + random.random()/2*(float(random.randint(-1,1)))
                location.sheep = sheep
                location.timestamp = dag
                location.temperature = (float(random.randint(384,400)))/10
                location.pulse = random.randint(60,90)
                location.save()
                longitude = location.longitude
                latitude = location.latitude
                dag = dag - timedelta(hours = 8)

        print "initiating...", i
    return render_to_response('index.html',
    {},
    context_instance=RequestContext(request))


def farmerRegister(request):
    logout(request)
    try:
        if request.POST['password2'] != request.POST['password3']:
            raise
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        password = request.POST['password2']
        username = request.POST['username2']
        farmer = Farmer.objects.create_user(username = username, password = password)
        farmer.first_name = first_name
        farmer.last_name = last_name
        farmer.is_staff = True
        farmer.user_permissions.add(20) #change user
        farmer.user_permissions.add(22) #add sheep
        farmer.user_permissions.add(23) #change sheep
        farmer.user_permissions.add(24) #delete sheep
        farmer.user_permissions.add(33) #delete location
        farmer.user_permissions.add(26) #change message
        farmerlist = Farmer.objects.all()
        if len(farmerlist) <= 2:
            for i in range(len(farmerlist)):
                farmerlist[i].farmerId = str(i+1).zfill(7)
                farmerlist[i].save()
        else:
            lastid = farmerlist[len(farmerlist)-2].farmerId
            farmer.farmerId = str(int(lastid) + 1).zfill(7)
            farmer.save()

        farmer = authenticate(username=username, password=password)
        if farmer is not None:
            login(request, farmer)
        else:
            raise
    except:
        return render_to_response('index_fail_register.html',
         {},
         context_instance=RequestContext(request))
    return HttpResponseRedirect('/farmer/farmer')

def farmer(request):
    if request.user.is_authenticated():
            farmer = request.user
    else:
        return HttpResponseRedirect('farmerLogin')
    return render_to_response('farmer/farmer.html',
        {'farmer':farmer},
        context_instance=RequestContext(request))

def farmerLogin(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        farmer = authenticate(username=username, password=password)
        if farmer is not None:
            login(request, farmer)
        else:
            raise
    except:
        return render_to_response('index_fail_login.html',
     {},
     context_instance=RequestContext(request))
    return render_to_response('farmer/farmer.html',
        {'farmer':farmer},
        context_instance=RequestContext(request))

def farmerLogout(request):
    if request.user.is_authenticated():
        farmer = request.user
        if farmer is not None:
            logout(request)
    return HttpResponseRedirect('/')

@login_required
def farmerUpdate(request):
    farmer = request.user
    try:
        result = "Please use correct telephone number."
        farmer.tlf = request.POST['tlf']
        result = "Reserve farmer does not exist."
        reserve_name = request.POST['reserve']
        farmer.reserve = Farmer.objects.get(username = reserve_name)
        farmer.save()
        result = "Update successfully!"
    except:
            return render_to_response('farmer/farmer_result.html',
        {'result':result,
         'farmer':farmer},
        context_instance=RequestContext(request))
    return render_to_response('farmer/farmer_result.html',
        {'result':result,
         'farmer':farmer},
        context_instance=RequestContext(request))
