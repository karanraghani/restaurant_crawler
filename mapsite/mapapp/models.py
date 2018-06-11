from django.db import models

# Create your models here.
class ZomCrawlerModel(models.Model):
	name = models.CharField(max_length=250)
	location = models.CharField(max_length=500)
	url = models.URLField()
	rating = models.CharField(max_length=10)

	def __str__(self):
		return self.name
