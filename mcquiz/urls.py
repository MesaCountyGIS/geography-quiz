from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^geographyquiz/admin/', include(admin.site.urls)),
    url(r'^geographyquiz/', include('geographyquiz.urls')),
)
