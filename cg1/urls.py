#regular imports
from django.conf.urls import patterns, include, url
from guides.views import guide_description, guide_page
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from statics.views import home

admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'creatorguides.views.home', name='home'),
	# url(r'^creatorguides/', include('creatorguides.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^$', home),
	url(r'^guides/$', guide_description),
	url(r'^guides/([0-9]+)/$', guide_description),
	url(r'^guides/([\w_]+)/$', guide_page),
        url(r'^admin/', include(admin.site.urls)),
)
