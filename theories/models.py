from django.db import models

class Theory(models.Model):
        theory_name = models.CharField(max_length=200, unique=True)
        
	def __unicode__():
                return theory_name
