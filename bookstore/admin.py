"""
AUTHOR      :   Robert James Patterson
DATE        :   11/10/2018
SYNOPSIS    :   Work thru file for 'Mastering Django: Core'. This file allows you to register
                your models with the django admin site which will give you default CRUD 
                operations. You can override the default behaivor of the display and the
                forms for theses operations here as well.
"""

from django.contrib import admin
from .models import Publisher, Author, Book


class AuthorAdmin(admin.ModelAdmin):
   
    # Select the columns from 'Author' to display.
    list_display = ('first_name', 'last_name', 'email')
   
    # Create a functional searchbar.
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    
    # Set display options for this class. 
    list_display = ('title', 'publisher', 'publication_date')
    
    # Create a functional list filter.
    list_filter = ['publication_date']
    
    # Create a hierarchial filter bar based on the publication_date.
    date_hierarchy = 'publication_date'
    
    # Sort the display of Book objects by publication_date.
    ordering = ['-publication_date']
    
    # Set the order the fields are displayed on the edit form. 
    #fields = ('title', 'authors', 'publisher', 'publication_date')
    
    # Override the default list-box behavior and use the 'Available/Chosen' box 
    # layout instead.
    filter_horizontal = ('authors',)

    #raw_id_fields = ('publisher',)

# Register our Model classes with the admin.site to provide default CRUD operations.
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
