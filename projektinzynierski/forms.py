from django import forms

class ConfigForm(forms.Form):
	old_password = forms.CharField(max_length=4)
