from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'projektinzynierski.views.home', name='home'),
    url(r'^alarm/', include('projektinzynierski.alarm.urls')),
    url(r'^light/', include('projektinzynierski.light.urls')),
    url(r'^multimedia/', include('projektinzynierski.multimedia.urls')),
    url(r'^admin/', include(admin.site.urls)),
	  url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
)
