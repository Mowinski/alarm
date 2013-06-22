from django.core.management.base import BaseCommand, CommandError
from projektinzynierski.alarm.models import Keyboard
from serial import Serial
import datetime

class Command(BaseCommand):
  args = '<keyboard id>'
  help = 'Identyfikator klawiatury z bazy danych'

  def handle(self, *args, **kwargs):
    try:
      id = int(args[0])
    except ValueError:
     raise CommandError('Nie podano poprawnego identyfikatora klawiatury')
    except IndexError:
     raise CommandError('Za malo parametrow')
    se = Serial('/dev/ttyAMA0')
    se.write('KD'+str(id));
    print 'KD'+str(id)
