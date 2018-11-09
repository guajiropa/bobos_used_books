"""
AUTHOR      :   Robert James Patterson
DATE        :   11/08/2018
SYNOPSIS    :   Work thru file for 'Mastering Django: Core'
"""
from django.contrib import admin
from .models import Publisher, Author, Book


class AuthorAdmin(admin.ModelAdmin):
    # Set display options for this class
    list_display = ('first_name', 'last_name', 'email')
    # Create a functional searchbar
    search_fields = ('first_name', 'last_name')


admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
