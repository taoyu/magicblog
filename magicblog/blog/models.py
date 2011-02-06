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


class PostManager(models.Manager):
    def search(self, search_string):
        search_string = search_string.strip()
        
        queryset = self.get_query_set()
        return queryset.filter(models.Q(title__icontains=search_string) | models.Q(body__icontains=search_string))


class Post(models.Model):
	author = models.ForeignKey(User, related_name='posts')
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	excerpt = models.TextField()
	published = models.BooleanField(default=False)
	pub_date = models.DateTimeField("Date Published")
	up_date = models.DateTimeField("Date Updated")
	categories = models.ManyToManyField(Category, blank=True, null=True)
	tags = models.ManyToManyField(Tag, blank=True, null=True)

	objects = PostManager()

    	@models.permalink
    	def get_absolute_url(self):
        	return ('single_post', [self.slug])

	def __unicode__(self):
		return self.title
	
	class Meta:
		ordering = ['-pub_date']



	
