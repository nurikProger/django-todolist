from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Tasks
from django.urls import reverse
# Create your views here.

def index(request):
	tasks = Tasks.objects.all().values()
	template = loader.get_template('index.html')
	context = {
	'tasks' : tasks,
	}
	return HttpResponse(template.render(context, request))

def changestatus(request, id):
	task = Tasks.objects.get(id=id)
	status = task.status 
	task.status = not(status)
	task.save()
	return HttpResponseRedirect(reverse('index'))

def delete(request, id):
	task = Tasks.objects.get(id=id)
	task.delete()
	return HttpResponseRedirect(reverse('index'))

def add(request):
	template = loader.get_template('add.html')
	return HttpResponse(template.render({}, request))

def addrecord(request):
	name = request.POST["taskname"]
	task = Tasks(name=name, status=False)
	task.save()
	return HttpResponseRedirect(reverse('index'))

def update(request, id):
	task = Tasks.objects.get(id=id)
	template = loader.get_template('update.html')
	context = {
	'task' : task,
	}
	return HttpResponse(template.render(context, request))

def updaterecord(request, id):
	taskname = request.POST['taskname']
	task = Tasks.objects.get(id=id)
	task.name = taskname
	task.save()
	return HttpResponseRedirect(reverse('index'))