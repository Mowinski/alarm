from django.core.management.base import BaseCommand, CommandError
from projektinzynierski.alarm.models import LoginAttempt, Keyboard
import datetime

class Command(BaseCommand):
  args = 'event_type keyboard_id'
  help = 'Typ eventu to: 1, 0'

  def handle(self, *args, **options):
    if not 'event_type' in args:
      raise CommandError('Nie podano typu akcji')
    if not 'keyboard_id' in args:
      raise CommandError('Nie podano sensora')
    event_type = args[args.index('event_type')+1]
    try:
      keyboard_id = int(args[args.index('keyboard_id')+1])
    except TypeError:
      raise CommandError('Identyfikator klawiatury musi byc liczba')

    if not ("1" == event_type or "0" == event_type):
      raise CommandError('Nie dozwolony typ akcji. Mozliwe akcje to 1 lub 0')

    try:
      keyboard = Keyboard.objects.get(pk=keyboard_id)
    except Keyboard.DoesNotExist:
      raise CommandError('Nie odnaleziono podanego sensora')
    event = LoginAttempt(keyboard=keyboard, date=datetime.datetime.now(), state=event_type)
    event.save()
    self.stdout.write('Dodano probe logowania')

