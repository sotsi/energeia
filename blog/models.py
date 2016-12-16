from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title
		
class Quest(models.Model):
	author = models.CharField(max_length=100)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title
		
class Question(models.Model):
	name = models.CharField(max_length=100)
	question = models.CharField(max_length=200)
	create_date = models.DateTimeField(
		default=timezone.now)
		

class Questions(models.Model):
	email = models.CharField(max_length=100)
	comment = models.TextField()
	create_date = models.DateTimeField(
		default=timezone.now)
