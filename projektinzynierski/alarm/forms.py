from django import forms
from projektinzynierski.alarm.models import Sensor, Keyboard


class KeyboardForm(forms.ModelForm):
  repassword = forms.CharField(label="Potwierdz haslo", max_length=6, widget=forms.PasswordInput(render_value=False))

  def __init__(self, *args, **kwargs):
    super(KeyboardForm, self).__init__(*args, **kwargs)
    self.fields['password'].widget = forms.PasswordInput(render_value=False)

  def clean(self):
    cleaned_data = super(KeyboardForm, self).clean()
    password = cleaned_data.get('password', '')
    repassword = cleaned_data.get('repassword', '')
    if len(password) < 1 or password != repassword:
      raise forms.ValidationError("Hasla musza byc takie same")
    try:
      int(password)
    except ValueError:
      raise forms.ValidationError("Haslo moze skladac sie tylko z cyfr")
    return cleaned_data

  class Meta:
    model = Keyboard

class SensorForm(forms.ModelForm):
  class Meta:
    model = Sensor
