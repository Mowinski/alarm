from django.contrib import admin
from projektinzynierski.alarm.models import Alarm, Sensor, Event, Keyboard, LoginAttempt

class AlarmAdmin(admin.ModelAdmin):
	fields = ['state', 'date', 'person']
	list_display = ('state', 'date')

class SensorAdmin(admin.ModelAdmin):
	fields = ['place', 'desc']
	list_dislpay = ('place',)

class EventAdmin(admin.ModelAdmin):
	fields = ['sensor', 'date', 'state',]
	list_display = ('sensor', 'date', 'state',)

class LoginAttemptAdmin(admin.ModelAdmin):
  pass

class KeyboardAdmin(admin.ModelAdmin):
  pass

admin.site.register(Alarm, AlarmAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(LoginAttempt, LoginAttemptAdmin)
admin.site.register(Keyboard, KeyboardAdmin)
