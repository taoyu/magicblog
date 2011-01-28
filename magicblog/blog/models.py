from django.db import models

from django.contrib.auth.models import User

from datetime import datetime

class Category(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Post(models.Model):
	author = models.ForeignKey(User, related_name='posts')
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	excerpt = models.TextField()
	published = models.BooleanField(default=False)
	pub_date = models.DateTimeField("Date Published", auto_now_add=True)
	up_date = models.DateTimeField("Date Updated", auto_now=True)
	categories = models.ManyToManyField(Category)
	tags = models.ManyToManyField(Tag)

	def __unicode__(self):
		return self.title



	
