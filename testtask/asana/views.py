from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as lin, logout as lout
from rest_framework.authtoken.models import Token
from .models import Task

def auth(cntr):
	def inner(request, *args, **kwargs):
		if request.user.is_authenticated:
			return cntr(request, *args, **kwargs)
		return render(request, 'login.html', {}) 
	return inner

@auth
def index(request):
	tasks = Task.objects.filter(user=request.user.id)
	args = dict(tasks=tasks, count=tasks.count())
	return render(request, 'tasks.html', args)

	

@auth
def api(request):
	token = Token.objects.get(user=request.user)
	if request.method == 'POST' and not(token):
		token = Token.objects.create(user=request.user)
	return render(request, 'api.html', dict(token=token))

def login(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)
	if user:
		lin(request, user)
		return redirect('index')
	args = dict(error='Неправильный пароль или имя')
	return render(request, 'login.html', args)

@auth
def logout(request):
	lout(request)
	return redirect('index')