from django.core.management.base import BaseCommand, CommandError
from projektinzynierski.alarm.models import Event, Sensor
import datetime
from serial import Serial

class Command(BaseCommand):
  args = '<sensor id>'
  help = 'Identyfikator sensora z bazy danych'

  def handle(self, *args, **kwargs):
    try:
      id = int(args[0])
    except ValueError:
      raise CommandError('Identyfikator musi byc liczba')
    except IndexError:
      raise CommandError('Zbyt malo parametrow')

    ser = Serial("/dev/ttyAMA0")
    ser.write('SD'+str(id))
    print 'SD'+str(id)
