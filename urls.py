from django.conf.urls.defaults import patterns,include, url
from django.contrib import admin
from mysite.views import hello

urlpatterns = patterns('',
	url(r'^hello/$', hello),
	url(r'^admin/', include(admin.site.urls)),

)