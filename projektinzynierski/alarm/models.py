from django.db import models
from django.contrib.auth.models import User

class Keyboard(models.Model):
  name = models.CharField('Nazwa klawiatury', max_length=40)
  port = models.CharField('Port na ktorym dziala klawiatura w centrali', max_length=5, unique=True)
  password = models.CharField('Haslo', max_length=6)

  def __unicode__(self):
    return self.name


class Alarm(models.Model):
	DISABLE = "DS"
	ENABLE = "EN"
	TURNON = "TON"
	TURNOFF = 'TOFF'
	ALARM_STATE = ( 
			(DISABLE, 'Alarm wylaczony'),
			(ENABLE, 'Alarm wlaczony'),
			(TURNON, 'Alarm wlaczono'),
			(TURNOFF, 'Alarm wylaczono'),
			)	
	state = models.CharField(max_length=4, choices=ALARM_STATE)
	date = models.DateTimeField('Czas zdazenia');
	person = models.ForeignKey(User)
	keyboard = models.ForeignKey(Keyboard)
	
	def __unicode__(self):
		return "{0}: {1} - {2}".format(self.id, self.get_state_display(), self.date)	



class Sensor(models.Model):
  place = models.CharField('Miejsce polozenia', max_length=120)
  desc = models.TextField('Opis czujnika (grupy czujnikow)')
  port = models.CharField('Port na ktorym pracuje urzadzenie w centrali', max_length=5, unique=True)

  def __unicode__(self):
		return "{0}".format(self.place)

class Event(models.Model):
  EVENT_STATE = (
    ('ON', 'Alarm wlaczono'),
    ('OFF', 'Alarm wylaczono'),
  )
  sensor = models.ForeignKey(Sensor)
  date = models.DateTimeField('Czas zdazenia')
  state = models.CharField(max_length=3, choices=EVENT_STATE)

  class Meta:
    permissions = (('can_view_event', 'Can view event'),)


class LoginAttempt(models.Model):
  ATTEMPT_STATE = (
    ('1', 'Correct password'),
    ('0', 'Password not correct'),
  )

  keyboard = models.ForeignKey(Keyboard)
  date = models.DateTimeField('Czas zdazenia')
  state = models.CharField(max_length=3, choices=ATTEMPT_STATE)

  class Meta:
    permissions = (('can_view_login_attempt', 'Can view login attempt'),)
