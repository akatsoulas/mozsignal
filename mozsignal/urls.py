from django.conf import settings
from django.conf.urls.defaults import patterns, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from funfactory.monkeypatches import patch
patch()

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Example:
    (r'', include('mozsignal.base.urls')),
    (r'^', include('mozsignal.base.urls')),

    # Admin
    (r'^admin/', include(admin.site.urls)),

    # Generate a robots.txt
    (r'^robots\.txt$',
        lambda r: HttpResponse(
            "User-agent: *\n%s: /" % 'Allow' if settings.ENGAGE_ROBOTS else 'Disallow',
            mimetype="text/plain"
            )),
)

# In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
