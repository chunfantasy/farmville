# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate

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
	if len(Farmer.objects.all()) != 0:
	    farmerlist = Farmer.objects.all()
	    lastid = farmerlist[-2].farmerid
	    farmer.farmerid = str(int(lastid) + 1)
	    farmer.save()
	else:
	    farmer.farmerid = '1000001'
	    farmer.save()
    except:
	return render_to_response('index.html',
	    {},
	    context_instance=RequestContext(request))
    return render_to_response('result.html',
	{'result':'Success'},
	context_instance=RequestContext(request))

def farmerLogin(request):
    try:
	username = request.POST['username']
	password = request.POST['password']
	print username
	print password
	farmer = authenticate(username=username, password=password)
	print farmer
	if farmer is not None:
	    result = 'success!'
	else:
	    result = 'fail!'
    except RuntimeError as e:
    	print e
    	result = 'error!'
    return render_to_response('result.html',
	{'result':result},
	context_instance=RequestContext(request))
    
