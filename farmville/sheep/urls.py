from django.conf.urls import patterns, include, url

urlpatterns = patterns('farmville.sheep.views',
    # Examples:
    # url(r'^$', 'farmville.views.home', name='home'),
    # url(r'^farmville/', include('farmville.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^sheepGenerateTest', 'sheepGenerateTest'),
    url(r'^sheepGenerate', 'sheepGenerate'),
    url(r'^sheepRegister', 'sheepRegister'),
    url(r'^sheepDelete', 'sheepDelete'),
    url(r'^sheepGetList', 'sheepGetList'),
    url(r'^getSheepLog', 'getSheepLog'),
    url(r'^getSheepDetail', 'getSheepDetail'),
    url(r'^sendMail', 'sendMail'),
)