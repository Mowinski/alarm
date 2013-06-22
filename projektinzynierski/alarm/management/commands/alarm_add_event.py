from django.core.management.base import BaseCommand, CommandError
from projektinzynierski.alarm.models import Event, Sensor
import datetime

class Command(BaseCommand):
  args = 'event_type sensor_id'
  help = 'Typ eventu to: ON, OFF'

  def handle(self, *args, **options):
    if not 'event_type' in args:
      raise CommandError('Nie podano typu akcji')
    if not 'sensor_id' in args:
      raise CommandError('Nie podano sensora')
    event_type = args[args.index('event_type')+1]
    try:
      sensor_id = int(args[args.index('sensor_id')+1])
    except TypeError:
      raise CommandError('Identyfikator sensora musi byc liczba')

    if not ("ON" in event_type or "OFF" in event_type):
      raise CommandError('Nie dozwolony typ akcji. Mozliwe akcje to ON lub OFF')

    try:
      sensor = Sensor.objects.get(pk=sensor_id)
    except Sensor.DoesNotExist:
      raise CommandError('Nie odnaleziono podanego sensora')
    event = Event(sensor=sensor, date=datetime.datetime.now(), state=event_type)
    event.save()
    self.stdout.write('Dodano event')

