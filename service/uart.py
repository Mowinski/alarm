#!/home/pi/python2.7/bin/python
from serial import Serial
from django.core.management import call_command
import os

ser = Serial("/dev/ttyAMA0")
while True:
  read = ser.read()
  if read == 'a':
    os.system("./alarm_state.py")
    read = ser.read()
    print read

  if read == 'd':
    os.system("./sensor_state.py")
    read = ser.read()
    print read

  if read == 'p':
    os.system("./keyboard_state.py")
    read = ser.read()
    print read

  if read == 'e':
    sensor_id = ser.read()
    state = ser.read()
    if state == 1:
      state = 'ON'
    else:
      state = 'OFF'
    os.system("../manage.py alarm_add_event event_type {0} sensor_id {1} &".format(state, sensor_id))
    ser.write('OK')

  if read == 'l':
    keyboard_id = ser.read()
    state = ser.read()
    os.system("../manage.py alarm_login_attempt event_type {0} keyboard_id {1} &".format(state, keyboard_id))
    ser.write('OK')

