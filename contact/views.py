# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import render
from contact.models import RegularSend
from contact.forms import RssForm
from contact.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.template import RequestContext
from django.conf import settings
from django.shortcuts import render_to_response, redirect
from django.contrib import messages
from django import forms
# Create your views here.
# -*- coding: utf-8 -*-

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
    	if form.cleaned_data["honeypot"] == "":
    		
	        form_email = form.cleaned_data.get("email")
	        form_message = form.cleaned_data.get("message")
	        form_full_name = form.cleaned_data.get("full_name")
	        subject = 'Письмо с сайта OZNA.SU со страницы КОНТАКТЫ'
	        from_email = settings.EMAIL_HOST_USER
	        to_email = [from_email, 'bogdanovv@skelektro.ru']
	        contact_message = "(     Имя: %s     )_______(     Сообщение: %s     )_______(     E-mail: %s     )" %(
	            form_full_name,
	            form_message,
	            form_email)
	
	        send_mail(subject,
	        contact_message,
	        from_email,
	        to_email,
	        fail_silently=True)
	        return HttpResponseRedirect('/thanks/')
    context = {
        "form":form,
    }
    return render(request, "form.html", context)

# Create your views here.

class ContactView(TemplateView):
	template_name = "contact.html"
	
class ThanksView(TemplateView):
	template_name = "thanks.html"


class ModelRssForm(forms.ModelForm):
	class Meta:
		model = RegularSend
		fields = ['name', 'email']
		labels = {'neme':'Имя', 'email':'Mail'}
	

def rssview(request):
    if request.method == 'post':
        form = ModelRssForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            rss = RegularSend()
            rss.name = data["name"]
            rss.email = data["email"]
            rss.save()
            messages.success(request, 'Отправлено')
            return redirect(rss)
            
    else:
        form = ModelRssForm()
    return render(request, 'rss.html', {'form': form})    
    
    
    
    

