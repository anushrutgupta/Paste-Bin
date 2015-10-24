from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^pastebin/', include('pastebin.urls', namespace = 'pastebin')),
    url(r'^admin/', include(admin.site.urls)),
)
