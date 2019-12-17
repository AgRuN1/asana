from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Task

def index(request):
	if request.user.is_authenticated:
		tasks = Task.objects.filter(user=request.user.id)
		args = dict(tasks=tasks, count=tasks.count())
		return render(request, 'tasks.html', args)

	return render(request, 'auth.html', {})

def auth(request):
	if request.user.is_authenticated:
		return redirect('index')

	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)
	if user:
		login(request, user)
		return redirect('index')
	args = dict(error='Неправильный пароль или имя')
	return render(request, 'auth.html', args)