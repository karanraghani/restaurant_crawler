from django.shortcuts import render
from mapapp.models import ZomCrawlerModel
import json

def index(request):
	restaurants = ZomCrawlerModel.objects.all()
	rest_list = [restaurant.name for restaurant in restaurants]
	#places =json.dumps({'place':rest_list})
	return render(request,'mapapp/index.html',{'places': rest_list,})
