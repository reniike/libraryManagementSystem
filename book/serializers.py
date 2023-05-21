from decimal import Decimal
from rest_framework import serializers
from book.models import Book, Author


class AuthorSerializer(serializers.Serializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'isbn', 'book_number', 'discounted_price']

    book_number = serializers.CharField(max_length=15, source='isbn')
    discounted_price = serializers.SerializerMethodField(method_name='calculate')

    def calculate(self, book: Book):
        return book.price * Decimal(0.1)
