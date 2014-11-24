from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import hello,now,futureHours,showName,showRequest

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myWebApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^now/$', now),
    url(r'^future/(\d{1,2})/$', futureHours),
    url(r'^nameis/([a-zA-Z]{1,10})/$', showName),
    url(r'^showreq/$',showRequest),
)
