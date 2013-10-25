from django.conf.urls import patterns, include, url
import farmville
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'farmville.views.home', name='home'),
    # url(r'^farmville/', include('farmville.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'farmville.farmer.views.index'),
    url(r'^initial$', 'farmville.farmer.views.initial'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^farmer/', include('farmville.farmer.urls')),
    url(r'^sheep/', include('farmville.sheep.urls')),
    #url(r'^message/$', include('farmville.message.urls')),
    #url(r'^wolf/$', include('farmville.wolf.urls')),
)
