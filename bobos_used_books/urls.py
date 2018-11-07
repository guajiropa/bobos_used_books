"""
AUTHOR      :   Robert James Patterson
DATE        :   11/03/2018
SYNOPSIS    :   Workthru file for 'Mastering Django: Core'
"""
from django.conf.urls import include, url
from django.contrib import admin
from bobos_used_books.views import index, hello, current_datetime, hours_ahead

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})$', hours_ahead),
    
]
