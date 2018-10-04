# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.shortcuts import render
from product.models import Product, Table, Category
# Create your views here.
# -*- coding: utf-8 -*-



# Create your views here.
class IndexView(TemplateView):
	template_name = "index.html"


class ProductView(TemplateView):
	template_name = "product.html"
	
class KtpView(ListView):
	model = Product
	template_name = "ktp.html"
	
def ktpview(request, service_id):
	args = {}
	args['name_context'] = Category.objects.get(id=service_id)
	args['context_filter'] = Product.objects.filter(category_id=service_id)
	return render_to_response('ktp.html', args)	



	

class DetailLampView(TemplateView):
	template_name = "detailsvet.html"

class DetailLedLampView(TemplateView):
	template_name = "ledsvet.html"
	



def productdetail(request, alias):
	args = {}
	
	args['name_context'] = Product.objects.get(alias=alias)
	
	return render_to_response('productdetail.html', args)





