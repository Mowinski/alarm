from django.core.management.base import BaseCommand, CommandError
from projektinzynierski.alarm.models import LoginAttempt, Keyboard
import datetime

class Command(BaseCommand):
  args = 'id port'
  help = 'Port jako PAx'

  def handle(self, *args, **options):
    
    pass

