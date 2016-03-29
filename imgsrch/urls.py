from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView, DetailView
from django.conf.urls.static import static

#from imgsrch import *
from mongoengine import *

from imgsrch.models import ImageDB
from imgsrch import views

#from minor import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
#image_list = ListView.as_view(model=ImageDB)
#image_detail = DetailView.as_view(model=ImageDB)

urlpatterns = patterns('',
	url(r'^test/$', views.test, name='test'),
    url(r'^$', views.Home.as_view(), name='Home'),
    url(r'^insert/$', views.insertDoc, name='insert'),
    url(r'^image_list/$', views.image_list, name='image_list'),
    url(r'^home/$', views.Home.as_view(), name='Home')
    # Examples:
    # url(r'^$', 'imgsrch.views.home', name='home'),
    # url(r'^imgsrch/', include('imgsrch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
