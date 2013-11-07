# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

from farmville.farmer.models import Farmer

common_names = ['Anne','Inger','Kari','Marit','Ingrid','Liv','Eva','Berit','Astrid',
                'Bjørg','Hilde','Anna','Solveig','Marianne','Randi','Ida','Nina',
                'Maria','Elisabeth','Kristin','Bente','Heidi','Silje','Hanne',
                'Jan','Per','Bjørn','Ole','Lars','Kjell','Knut','Arne','Svein',
                'Thomas','Hans','Geir','Tor','Morten','Terje','Odd','Erik','Martin',
                'Andreas','John','Anders','Rune','Trond','Tore','Daniel','Jon']

def index(request):
    return render_to_response('index.html',
    {},
    context_instance=RequestContext(request))

def initiate(request):
    farmerlist = Farmer.objects.all()
    if len(farmerlist) <= 2:
        for i in range(len(farmerlist)):
        	f = farmerlist[i]
                f.farmerId = str(i+1).zfill(7)
                f.save()
    lastid = len(farmerlist)
    for i in range(len(common_names)):
        name = common_names[i]
        username = name + "@farmville.com"
        password = "1"
        farmer = Farmer.objects.create_user(username = username, password = password)
        farmer.first_name = name
        farmer.last_name = name
        farmer.farmerId = str(int(lastid) + int(i) + 1).zfill(7)
        farmer.is_staff == True
        farmer.user_permissions.add(20) #change user
        farmer.user_permissions.add(22) #add sheep
        farmer.user_permissions.add(23) #change sheep
        farmer.user_permissions.add(24) #delete sheep
        farmer.user_permissions.add(31) #add location
        farmer.user_permissions.add(33) #delete location
        farmer.save()
	print "initiating..."
    return render_to_response('index.html',
    {},
    context_instance=RequestContext(request))

def farmerRegister(request):
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

        farmerlist = Farmer.objects.all()
        print len(farmerlist)
        if len(farmerlist) <= 2:
            for i in range(len(farmerlist)):
                farmerlist[i].farmerId = str(i+1).zfill(7)
                farmerlist[i].save()
        else:
            lastid = farmerlist[len(farmerlist)-2].farmerId
            farmer.farmerId = str(int(lastid) + 1).zfill(7)
            farmer.save()
    except:
        return render_to_response('index_fail_register.html',
	    {},
	    context_instance=RequestContext(request))
    return render_to_response('farmer/farmer.html',
	{'farmer': farmer},
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
