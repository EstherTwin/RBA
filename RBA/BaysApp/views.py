from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html')

def schedule(request):
	return render(request, 'schedule.html')
