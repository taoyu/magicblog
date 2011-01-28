from django.conf.urls.defaults import *
from magicblog.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^magicblog/', include('magicblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^$', static_page, {'template' : 'base'}),

    url(r'^(?P<template>\w+)/$', static_page, name="static_page"),
)
