# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from farmville.farmer.models import Farmer

def index(request):
	return render_to_response('index.html',
	{},
	context_instance=RequestContext(request))

def farmerRegister(request):
	farmer = Farmer()
	farmer.username = request.POST['username']
	if len(Farmer.objects.all()) != 0:
	    	farmerlist = Farmer.objects.all()
	    	lastid = farmerlist[len(farmerlist)-1].farmerid
		farmer.farmerid = str(int(lastid) + 1)
		farmer.save()
	else:
	    	farmer.farmerid = '1000001'
		farmer.save()
	print farmer
	return render_to_response('farmer/farmer_register.html',
		{},
		context_instance=RequestContext(request))

def farmerLogin(request):
	username = request.POST['username']
	password = request.POST['password']
	farmer = Farmer.objects.get(username = username)
	if password == farmer.password:
		result = 'success!'
	else:
		result = 'fail!'
	return render_to_response('result.html',
		{'result':result},
		context_instance=RequestContext(request))
    
