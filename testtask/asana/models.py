from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	title = models.CharField(max_length=200)
	def __str__(self):
		return self.title

class Task(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	txt = models.TextField()
	def __str__(self):
		return self.txt[:50]