from django.db import models

# Create your models here.

class Comic(models.Model):
	title = models.TextField()
	cover = models.URLField()
	price = models.FloatField()
	brand = models.CharField(max_length=100)
	ident = models.CharField(max_length=100)
	notes = models.TextField()


