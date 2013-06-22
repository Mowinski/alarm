from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'projektinzynierski.multimedia.views.home', name='multimedia_home'),
)
