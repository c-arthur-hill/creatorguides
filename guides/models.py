from django.db import models
from groupings.models import Grouping
from theories.models import Theory
class Guide (models.Model):
	guide_name = models.CharField(max_length=50)
	guide_page = models.CharField(max_length=60, blank=True)
	guide_graphic_name = models.CharField(max_length=50)
	guide_created = models.DateTimeField(auto_now_add=True, blank=True)
	guide_description = models.CharField(max_length=500)
	guide_content = models.TextField()
	pay = models.BooleanField()
	guide_views = models.PositiveIntegerField(default=0, blank=True)
	guide_votes = models.PositiveIntegerField(default=0, blank=True)
	guide_meta = models.ForeignKey(Grouping, blank=True, null=True)
	guide_knowledge = models.ForeignKey(Theory, blank=True, null=True)
	def __unicode__(self):
		return self.guide_name

	class Meta:
		ordering = ['guide_created']
		permissions = (("access_pay", "can access paid guides"),) 
