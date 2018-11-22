"""
AUTHOR      :   Robert James Patterson
DATE        :   11/03/2018
SYNOPSIS    :   Workthru file for 'Mastering Django: Core'
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import hello, index, current_datetime, hours_ahead, display_meta, contact
from bookstore import views

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})$', hours_ahead),
    url(r'^display-meta/$', display_meta),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact/$', contact),
]
