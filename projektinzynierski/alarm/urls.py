from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'projektinzynierski.alarm.views.home', name='alarm_home'),
    url(r'^history/$', 'projektinzynierski.alarm.views.history', name='alarm_history'),
    url(r'^sensor/$', 'projektinzynierski.alarm.views.sensor', name='alarm_sensor'),
    url(r'^sensor/(?P<sensor_id>\d+)/(?P<action>[E,D])/$', 'projektinzynierski.alarm.views.sensor', name='alarm_sensor'),
    url(r'^keyboard/$', 'projektinzynierski.alarm.views.keyboard', name='alarm_keyboard'),
    url(r'^keyboard/(?P<keyboard_id>\d+)/(?P<action>[E,D])/$', 'projektinzynierski.alarm.views.keyboard', name='alarm_keyboard'),
)
