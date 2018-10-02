

from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from product.models import Product, Category

register = template.Library()

@register.inclusion_tag('tags/product_tag.html')
def contact_address(id):
	data = Product.objects.get(pk=int(id))
	return {'data':data}
	
@register.inclusion_tag('tags/product_menu.html')
def prodact_menu():
	data = Category.objects.all()
	return {'data':data}