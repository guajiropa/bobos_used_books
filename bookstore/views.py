"""
AUTHOR      :   Robert James Patterson
DATE        :   11/10/2018
SYNOPSIS    :   Work-thru file for 'Mastering Django: Core'.
"""

from django.shortcuts import render
from django.http import HttpResponse


def search_form(request):

    return render(request, 'search_form.html')

def search(request):

    if 'q' in request.GET:
        message = "You searched for:  %r ." % request.GET['q']
    else:
        message = "You submitted an empty form."

    return HttpResponse(message)
