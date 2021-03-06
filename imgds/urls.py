from django.conf.urls.defaults import *

urlpatterns = patterns('imgds.views',
    url(r'^$','index'),
    url(r'^browse/(?P<category>\w+)/$', 'browse', name='category'),
    url(r'^browse/(?P<category>\w+)/(?P<softwareid>\w+)/$', 'browse', name='browse'),
    url(r'^search/', 'search', name='search'),
    )
