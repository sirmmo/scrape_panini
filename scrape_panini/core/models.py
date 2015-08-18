from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Comic(models.Model):
	title = models.TextField()
	cover = models.URLField()
	price = models.FloatField()
	brand = models.CharField(max_length=100)
	ident = models.CharField(max_length=100)
	notes = models.TextField(null=True, blank=True)
	contains = models.TextField(null=True, blank=True)

	year = models.IntegerField()
	week = models.IntegerField()

	def __str__(self):
		return self.title

	class Meta:
		ordering=["-year", "-week"]

class Collection(models.Model):
	owner = models.ForeignKey(User, related_name="owned_by")
	comic = models.ForeignKey(Comic, related_name="owned_by")
	the_list = models.TextField(default="collection")

class Tag(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class ComicTag(models.Model):
	tag = models.ForeignKey(Tag)
	comic = models.ForeignKey(Comic, related_name="tagged_with")



