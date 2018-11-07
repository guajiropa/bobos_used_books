"""
AUTHOR      :   Robert James Patterson
DATE        :   11/03/2018
SYNOPSIS    :   Work-thru file for Chapter 2 from 'Mastering Django: Core'
"""
from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import Http404, HttpResponse

def hello(request):
    return HttpResponse("Hello Django World!")

def index(request):
    return HttpResponse("This is where your homepage belongs!")

def current_datetime(request):
    now = datetime.now()
    return render(request, 'current_datetime.html', {'current_datetime': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
   
    dt = datetime.now() + timedelta(hours=offset)
    
    return render(request, 'hours_ahead.html', {'hours_offset': offset, 'next_time': dt})
