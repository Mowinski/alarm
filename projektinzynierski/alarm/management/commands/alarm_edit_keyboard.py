from django.core.management.base import BaseCommand, CommandError
from projektinzynierski.alarm.models import Keyboard
import datetime
from serial import Serial

class Command(BaseCommand):
  args = '<keyboard id>'
  help = 'Identyfikator klawiatury z bazy danych'

  def handle(self, *args, **kwargs):
    try:
      id = int(args[0])
      keyboard = Keyboard.objects.get(pk=id)
    except ValueError:
      raise CommandError('Identyfikator musi byc liczba')
    except IndexError:
      raise CommandError('Zbyt malo parametrow')
    except Keyboard.DoesNotExist:
      raise CommandError('Brak podanej klawiatury')

    ser = Serial("/dev/ttyAMA0")
    ser.write('K'+str(id)+keyboard.port+'H'+keyboard.password)
    print 'K'+str(id)+keyboard.port+'H'+keyboard.password
