# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import ContextMixin
from contact.models import RegularSend
from contact.views import ModelRssForm




class MainView(TemplateView):
    model = RegularSend
    template_name = "rss.html"
    form = None
    def get(self, request, *args, **kwargs):
        self.form = ModelRssForm()
        return super(MainView, self).get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context["form"] = self.form
        return context
    def post(self, request, *args, **kwargs):
        self.form = ModelRssForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return redirect("rss")
        else:
            return super(MainView, self).get(request, *args, **kwargs)	
    


class CategoryListMixin(ContextMixin):
  def get_context_data(self, **kwargs):
    context = super(CategoryListMixin, self).get_context_data(**kwargs)
    context["current_url"] = self.request.path

    return context


class OrderView(TemplateView):
    model = RegularSend
    template_name = "order.html"
    form = None
    def get(self, request, *args, **kwargs):
        self.form = OrderForm()
        return super(OrderView, self).get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
    	
        context = super(OrderView, self).get_context_data(**kwargs)
        context["form"] = self.form
        return context
    def post(self, request, *args, **kwargs):
        self.form = OrderForm(request.POST)
        if self.form.is_valid():
            if self.form.cleaned_data["honeypot"] == "":
                if self.form['qty'] > 0:
                    self.form.save()
                    messages.add_message(request, messages.SUCCESS, "Заказ успешно отправлен.")
                return redirect("main")
        else:
            return super(OrderView, self).get(request, *args, **kwargs)