# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

from farmville.farmer.models import Farmer

def index(request):
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
        if len(farmerlist != 0:
            print("BALARLARSKHKGHSAKJSKJGFAKS")
            lastid = farmerlist[0].farmerid
            farmer.farmerid = str(int(lastid) + 1).zfill(7)
            farmer.save()
        else:
            print "BALARLARSKHKGHSAKJSKJGFAKS"
            farmer.farmerid = '1'.zfill(7)
            farmer.save()
    except RuntimeError as e:
        print e
        return render_to_response('index_fail_register.html',
	    {},
	    context_instance=RequestContext(request))
    return render_to_response('result.html',
	context_instance=RequestContext(request))

def farmerLogin(request):
    try:
	username = request.POST['username']
	password = request.POST['password']
	farmer = authenticate(username=username, password=password)
	if farmer is not None:
	    print farmer
	    login(request, farmer)
	    result = 'success!'
	    print "success"
	else:
	    raise
    except:
    	return render_to_response('index_fail_login.html',
	    {},
	    context_instance=RequestContext(request))
    return render_to_response('result.html',
	{'result':result},
	context_instance=RequestContext(request))
    
