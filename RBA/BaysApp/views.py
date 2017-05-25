from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.shortcuts import render
from .forms import UserLoginForm
from BaysApp.models import Schedule,BayAllocation

from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
	title ="Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
	   username = form.cleaned_data.get("username")
	   password = form.cleaned_data.get("password")
	   user = authenticate(username=username, password=password)
	   login(request, user)
	   #return redirect('path')
	return render(request, 'form.html')

def logout_view(request):
	return render(request, 'form.html', {"form": form, "title": title})

def home(request):
	return render(request, 'homepage.html')

def schedule(request):
	data = BayAllocation.objects.all()
	return render(request, 'BayA.html', {"data" : data})
def load(request):
	return render(request, 'load.html')
#@login_required
def index(request):
	data = Schedule.objects.all()
	return render(request, 'index2.html', {"data" : data})
