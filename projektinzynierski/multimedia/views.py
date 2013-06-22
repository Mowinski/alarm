from django.shortcuts import render_to_response
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.template import RequestContext
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.forms.util import ErrorList

@login_required
def home(request):
	form = AuthenticationForm()
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			login(request, form.get_user())
	return render_to_response('home.html', {'form': form}, context_instance=RequestContext(request))



