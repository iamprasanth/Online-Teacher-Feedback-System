#!python
#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

#def email_check(user):
#    return user.email.endswith('@teacher.com')


# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating

@login_required(login_url="login/")
def home(request):
		if not request.user.email.endswith('@teacher.com') :
			return render(request,"home.html")
		elif request.user.email.endswith('@teacher.com') :
			return render(request,"results.html")