# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import render
from ozna.views import CategoryListMixin

# Create your views here.
# -*- coding: utf-8 -*-



# Create your views here.

class NewsView(TemplateView, CategoryListMixin):
	template_name = "news.html"
    
