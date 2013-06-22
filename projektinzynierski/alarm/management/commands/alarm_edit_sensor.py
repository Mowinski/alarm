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
      sensor = Sensor.objects.get(id=id)
    except ValueError:
      raise CommandError('Identyfikator musi byc liczba')
    except IndexError:
      raise CommandError('Zbyt malo parametrow')
    except Sensor.DoesNotExist:
      raise COmmandError('Brak podanego czujnika')

    ser = Serial("/dev/ttyAMA0")
    ser.write('S'+str(id)+sensor.port)
    print 'S'+str(id)+sensor.port
