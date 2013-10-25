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

def initial(request):
    farmerlist = Farmer.objects.all()
    if len(farmerlist) <= 2:
        for i in range(len(farmerlist)):
                farmerlist[i].farmerid = str(i+1).zfill(7)
                farmerlist[i].save()
    lastid = len(farmerlist)
    for i in range(len(common_names)):
        name = common_names[i]
        username = name + "@farmville.com"
        password = "1"
        farmer = Farmer.objects.create_user(username = username, password = password)
        farmer.first_name = name
        farmer.last_name = name
        farmer.farmerId = str(int(lastid) + int(i) + 1).zfill(7)
        farmer.save()
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
                farmerlist[i].farmerid = str(i+1).zfill(7)
                farmerlist[i].save()
        else:
            lastid = farmerlist[len(farmerlist)-2].farmerid
            farmer.farmerid = str(int(lastid) + 1).zfill(7)
            farmer.save()
    except:
        return render_to_response('index_fail_register.html',
	    {},
	    context_instance=RequestContext(request))
    return render_to_response('result.html',
	{'result':'success!'},
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
    
