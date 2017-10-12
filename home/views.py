from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import MenuItem

# Create your views here.

def index(request):
	itemList = MenuItem.objects.all()
	template = loader.get_template('home/index.html')
	context = {
		'itemList' : itemList
	}
	# return HttpResponse("Views.py is running")
	return HttpResponse(template.render(context, request))