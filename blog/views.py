# Create your views here.
from models import Dakbill, Comment 
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
def home(request):
    	dakbill = Dakbill.objects.get(pk=1)
	t = loader.get_template('base.html')
	c = Context({'dakbill':dakbill })
	return HttpResponse(t.render(c))


	
