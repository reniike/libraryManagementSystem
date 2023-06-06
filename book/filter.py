from django_filters import FilterSet

from book.models import Author, Book


class AuthorFilter(FilterSet):
    class Meta:
        model = Author
        fields = {
            'first_name': ['exact']
        }


class BookFilter(FilterSet):
    model = Book
    fields = {
        'title' : ['exact'],
        'price' : ['gt', 'lt']
    }
