from django.contrib import admin
from django.shortcuts import render

import book
from .models import Author, Book


# Register your models here.
#

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_filter = ['email']
    list_per_page = 10


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'language', 'genre']
    list_per_page = 10


# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book, BookAdmin)
