from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^plot/', include('plotato.plots.urls')),
       (r'^', include('plotato.projects.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # needed for development server
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()