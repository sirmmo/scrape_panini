from django.conf.urls import patterns, include, url
from django.contrib import admin

from core.api import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scrape_panini.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


    url(r'^$', 'core.views.collection'),
    url(r'^collection$', 'core.views.collection'),

    url(r'^collection/(?P<user>\w+)$', 'core.views.collection'),
    url(r'^collection/(?P<user>\w+)/wishlist$', 'core.views.collection', {"clist":"wishlist"}),

    url(r'^add$', 'core.views.add'),
    url(r'^remove$', 'core.views.rem'),

    url(r'^accounts/profile/', "core.views.profile"),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout$', 'core.views.logout'),

    url(r'^api/', include(v1_api.urls)),

  

)
