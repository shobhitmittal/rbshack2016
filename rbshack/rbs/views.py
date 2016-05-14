from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse 
from django.shortcuts import render_to_response
from django.template import RequestContext, loader, Context
import models
from django.conf import settings
import os
import json
import time
import re
from lxml import etree

def landing(request):
	my_context={}
	return render_to_response('home.html',my_context,context_instance=RequestContext(request))

def login(request):
	print request.method
	print request.POST
	return HttpResponse('HSAISbni')

def test(request):
	print request
	return HttpResponse('sdfds')