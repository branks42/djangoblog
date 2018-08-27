from django.conf.urls import url
from . import views

# These url patterns only work on old versions of Django/Update with 'path' in future versions...
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^/details/(?P<id>\d+)/$', views.details, name='details')
]
