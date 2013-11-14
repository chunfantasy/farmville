# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('farmville.location.views',
    # Examples:
    # url(r'^$', 'farmville.views.home', name='home'),
    # url(r'^farmville/', include('farmville.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^locationMove$', 'locationMove'),
    url(r'^locationMoveAll$', 'locationMoveAll'),
)