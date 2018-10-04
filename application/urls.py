"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from ozna.views import MainView

from contact.views import ContactView
from contact.views import ThanksView
from news.views import NewsView
from about.views import AboutView
from product.views import ProductView
from product.views import KtpView
from product.views import  productdetail, ktpview, IndexView


from gear.views import GearView

from contact.views import contact, rssview


urlpatterns = [
    url(r'^pkf/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="main"),
    url(r'^contacts/$', ContactView.as_view(), name="contacts"),
    url(r'^news/$', NewsView.as_view(), name="news"),
    url(r'^about/$', AboutView.as_view(), name="about"),
    url(r'^product/$', ProductView.as_view(), name="product"),
    url(r'^product/(?P<service_id>\d+)/$', ktpview, name="ktp"),
    url(r'^gear/$', GearView.as_view(), name="gear"),
    url(r'^form/$', contact, name="form"),
    url(r'^thanks/$', ThanksView.as_view(), name="thanks"),
    url(r'^product/(?P<alias>[^/]+)/$', productdetail, name = 'productdetail'),
    url(r'^rss/$', MainView, name ='rss'),
	
]
