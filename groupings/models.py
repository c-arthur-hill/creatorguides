from django.db import models

class Grouping(models.Model):
	grouping_name = models.CharField(max_length=200, unique=True)

	def __unicode__(self):
		return self.grouping_name	
