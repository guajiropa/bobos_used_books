"""
AUTHOR      :   Robert James Patterson
DATE        :   11/10/2018
SYNOPSIS    :   Work-thru file for 'Mastering Django: Core'.
"""

from django.shortcuts import render
from django.http import HttpResponse
from bookstore.models import Book


def search_form(request):

    return render(request, 'search_form.html')

def search(request):
    
    errors = []

    if 'q' in request.GET:
        q = request.GET['q']
        if not q: 
            errors.append('Please enter a valid search term.')
        elif len(q) > 20:
            errors.append('Please enter a search term of 20 characters or less.')
        else: 
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
        return render (request, 'search_form.html', {'errors': errors})
