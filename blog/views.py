# Create your views here.
from models import Dakbill, Comment 
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.forms import ModelForm
@csrf_exempt
def home(request):
    	wanted_bill = Dakbill.objects.get(pk=1)
    	
	t = loader.get_template('base.html')
	comment=Comment(dakbill=wanted_bill)	
	form = CommentForm(request.POST,instance=comment)
	c = Context({'dakbill':wanted_bill,'form':form })
	return HttpResponse(t.render(c))
class CommentForm(ModelForm):
	class Meta:
		model=Comment
		exclude=['dakbill']
		exclude=['author']
