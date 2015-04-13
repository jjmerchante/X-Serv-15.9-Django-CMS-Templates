from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'myproject.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^files/(?P<path>.*)$',
                           'django.views.static.serve',
                           {'document_root': 'files'}),
                       url(r'^logout/', 'django.contrib.auth.views.logout'),
                       url(r'^annotated/(.*)$',
                           "cms_users_put.views.mostrarPlantilla"),
                       url(r'^(.*)$', "cms_users_put.views.mostrar"),
                       )
