from django.conf.urls import patterns, url

from pastebin import views

urlpatterns = patterns('',
    url(r'^$', views.paste_create, name = 'create'),
    url(r'^(?P<key>\w+)/$', views.paste_get, name='view'),
    url(r'^fork/(?P<key>\w+)/$', views.paste_fork, name='fork'),
)
