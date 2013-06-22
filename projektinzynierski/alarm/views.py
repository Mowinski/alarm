from django.shortcuts import render_to_response, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import permission_required
from django.template import RequestContext
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.management import call_command

from projektinzynierski.alarm.models import Event, Sensor, Keyboard, LoginAttempt
from projektinzynierski.alarm.forms import KeyboardForm, SensorForm

import logging
import datetime
log = logging.getLogger(__name__)

@login_required
def home(request):
	form = AuthenticationForm()
	return render_to_response('alarm/home.html', {
              'form': form
              }, context_instance=RequestContext(request))

@login_required
def history(request):
  event_list = Event.objects.all().order_by('date')
  attempt_list = LoginAttempt.objects.all().order_by('date')

  event_list  = list(event_list)
  attempt_list = list(attempt_list)
  display_list = list()
  while len(event_list) > 0 or len(attempt_list) > 0:
    try:
      event_list_date = event_list[0].date
    except IndexError:
      event_list_date = datetime.datetime.min

    try:
      attempt_list_date = attempt_list[0].date
    except IndexError:
      attempt_list_date = datetime.datetime.min


    if event_list_date > attempt_list_date:
      display_list.append(event_list.pop())
    else:
      display_list.append(attempt_list.pop())
  return render_to_response('alarm/history.html', {
              'list': display_list,
              }, context_instance=RequestContext(request))


# @TODO zadbac o prawa
@login_required
def sensor(request, sensor_id=None, action=None):
  if request.method == 'POST':
    # Edycja sensora
    if action == 'E':
      try:
        sensor_id = int(sensor_id)
      except ValueError:
        raise Http404
      sensor = Sensor.objects.get(pk=sensor_id)
      sensor_form = SensorForm(instance=sensor, data=request.POST)
    else:
      sensor_form = SensorForm(request.POST)
    if sensor_form.is_valid():
      sens = sensor_form.save()
      call_command("alarm_edit_sensor", sens.pk)
      return redirect('alarm_sensor')
  else:
    if action == 'E':
      try:
        sensor_id = int(sensor_id)
      except ValueError:
        raise Http404

      try:
        sensor = Sensor.objects.get(pk=sensor_id)
      except Sensor.DoesNotExist:
        raise Http404
      sensor_form = SensorForm(instance=sensor)
    else:
      sensor_form = SensorForm()

  if action == 'D':
    try:
      sensor_id = int(sensor_id)
    except ValueError:
      raise Http404

    try:
      sensor = Sensor.objects.get(pk=sensor_id)
    except Sensor.DoesNotExist:
      raise Http404
    sensor.delete()
    call_command('alarm_delete_sensor', sensor_id)
    return redirect('alarm_sensor')

  sensor_list = Sensor.objects.all()
  return render_to_response('alarm/sensor.html', {
              'sensor_list': sensor_list,
              'sensor_form': sensor_form,
              }, context_instance=RequestContext(request))


# @TODO zadbac o prawa
@login_required
def keyboard(request, keyboard_id=None, action=None):
  if request.method == 'POST':
    if action == 'E':
      try:
        keyboard_id = int(keyboard_id)
      except ValueError:
        raise Http404
      keyboard = Keyboard.objects.get(pk=keyboard_id)
      keyboard_form = KeyboardForm(instance=keyboard, data=request.POST)
    else:
      keyboard_form = KeyboardForm(request.POST)
    if keyboard_form.is_valid():
      key = keyboard_form.save()
      call_command("alarm_edit_keyboard", key.id);
      return redirect('alarm_keyboard')
  else:
    if action == 'E':
      try:
        keyboard_id = int(keyboard_id)
      except ValueError:
        raise Http404

      try:
        keyboard = Keyboard.objects.get(pk=keyboard_id)
      except Keyboard.DoesNotExist:
        raise Http404
      keyboard_form = KeyboardForm(instance=keyboard)
    else:
      keyboard_form = KeyboardForm()

  if action == 'D':
    try:
      keyboard_id = int(keyboard_id)
    except ValueError:
      raise Http404

    try:
      keyboard = Keyboard.objects.get(pk=keyboard_id)
    except Keyboard.DoesNotExist:
      raise Http404
    keyboard.delete()
    call_command('alarm_delete_keyboard', keyboard_id)
    return redirect('alarm_keyboard')

  keyboard_list = Keyboard.objects.all()
  return render_to_response('alarm/keyboard.html', {
              'keyboard_list': keyboard_list,
              'keyboard_form': keyboard_form,
              }, context_instance=RequestContext(request))



