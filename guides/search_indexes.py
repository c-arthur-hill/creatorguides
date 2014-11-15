from django.utils import timezone
from haystack import indexes
from guides.models import Guide
        

class GuideIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    created = indexes.DateTimeField(model_attr="guide_created")
    views = indexes.IntegerField(model_attr="guide_views")
    votes = indexes.IntegerField(model_attr="guide_votes")

    def get_model(self):
        return Guide

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(guide_created__lte=timezone.now())
