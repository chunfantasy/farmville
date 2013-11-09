# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from farmville.farmer.models import Farmer
from farmville.sheep.models import Sheep
from farmville.location.models import Location
from datetime import datetime
from datetime import timedelta
from datetime import date
import random

common_names = ['Anne','Inger','Kari','Marit','Ingrid','Liv','Eva','Berit','Astrid',
                'Bjørg','Hilde','Anna','Solveig','Marianne','Randi','Ida','Nina',
                'Maria','Elisabeth','Kristin','Bente','Heidi','Silje','Hanne',
                'Jan','Per','Bjørn','Ole','Lars','Kjell','Knut','Arne','Svein',
                'Thomas','Hans','Geir','Tor','Morten','Terje','Odd','Erik','Martin',
                'Andreas','John','Anders','Rune','Trond','Tore','Daniel','Jon']

def index(request):
    if request.user.is_authenticated():
            return HttpResponseRedirect('/farmer/farmer')
    return render_to_response('index.html',
    {},
    context_instance=RequestContext(request))

@login_required
def initiate(request):
    names = common_names[::]
    farmerlist = Farmer.objects.all()
    if len(farmerlist) <= 2:
        for i in range(len(farmerlist)):
            f = farmerlist[i]
            f.farmerId = str(i+1).zfill(7)
            f.save()
    lastid = len(farmerlist)
    for i in range(5):
        name = common_names[i]
        username = name + "@farmville.com"
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
        farmer.user_permissions.add(31) #add location
        farmer.user_permissions.add(33) #delete location
        farmer.save()
        for j in range(5):
            sheep = Sheep()
            sheep.farmer = farmer
            sheep.name = names[random.randint(0,49)]
            sheep.birthday = date.today()
            sheep.sheepId = farmer.farmerId + str(sheep.birthday)[3] + str(lastid+ i).zfill(4)
            sheep.birthplace = sheep.name + "stad"
            sheep.status = 0
            sheep.latitude = 59.5 + random.random()
            sheep.longitude = 8.5 + random.random()
            sheep.save()
            dag = datetime(2013,11,20,12,0,0,0)
            dag2 = datetime(2013,11,20,8,0,0,0)
            for k in range(5):
                location = Location()
                location.latitude = sheep.latitude
                location.longitude = sheep.longitude
                location.sheep = sheep
                location.tidspunkt = dag
                location.save()
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
        farmer.user_permissions.add(31) #add location
        farmer.user_permissions.add(33) #delete location
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
