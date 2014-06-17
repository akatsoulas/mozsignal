from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url(r'^browserid/', include('django_browserid.urls')),
    url(r'^$', 'mozsignal.base.views.main', name='main'),
)
