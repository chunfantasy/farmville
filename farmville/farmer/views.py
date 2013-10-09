# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from farmville.farmer.models import Farmer

def farmerRegister(request):
    return render_to_response('farmer/farmer_register.html',
    {},
    context_instance=RequestContext(request))

def farmerRegisterSubmit(request):
    farmer = Farmer()
    farmer.username = request.POST['username']
    if len(Farmer.objects.all()) != 0:
    	farmerlist = Farmer.objects.all()
	farmlist.delete()
    	print farmerlist
    else:
    	farmer.userid = '0000001'
    farmer.save()
    print farmer.username
    return render_to_response('farmer/farmer_register.html',
    {},
    context_instance=RequestContext(request))
