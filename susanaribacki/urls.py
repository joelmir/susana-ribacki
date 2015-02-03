# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'susanaribacki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', 'core.views.contact', name='contact'),
    url(r'^$', 'core.views.home', name='home'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)