from django.shortcuts import render_to_response
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.template import RequestContext
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.forms.util import ErrorList

from projektinzynierski.alarm.models import Event, Sensor

import logging
log = logging.getLogger(__name__)

def home(request):
	form = AuthenticationForm()
	return render_to_response('home.html', {'form': form}, context_instance=RequestContext(request))

def add_event(request, sensor_id, state='error'):
	user = authenticate(username='systemcontrol', password=passwd)
	if user is not None:
		log.warning("Alarms!!!")
		sensor = Sensor.objects.get(id=sensor_id)
		event = Event()
		event.sensor = sensor
		event.date = datetime.now()
		event.state = state.upper()
	else:
		log.error("Someone cant hack us!")

