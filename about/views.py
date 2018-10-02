# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import render
# Create your views here.
# -*- coding: utf-8 -*-



# Create your views here.

class AboutView(TemplateView):
	template_name = "about.html"