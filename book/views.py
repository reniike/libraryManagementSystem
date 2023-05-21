from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .filter import AuthorFilter
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from .pagination import DefaultPagination

# Create your views here.
from .serializers import AuthorSerializer


# class AuthorList(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#     def get_serializer_class(self):
#         return {"request": self.request}
# serializer = AuthorSerializer(authors, many=True)
# return Response(serializer.data, status=status.HTTP_200_OK)

# serializer = AuthorSerializer(data=request.data)
# serializer.is_valid(raise_exception=True)
# serializer.save()
# return Response('success', status=status.HTTP_201_CREATED)

# class BookList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get_serializer_class(self):
#         return {"request": self.request}

# def get(self, request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     serializer = AuthorSerializer(author)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# def put(self, request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     serializer = AuthorSerializer(author, data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response("Details updated", status=status.HTTP_201_CREATED)
#
# def delete(self, request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     if author.book_set.count() > 0:
#         return Response("Author is associated with a book and cannot be deleted", status=status.HTTP_200_OK)
#     author.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

# class ListOfBooks(APIView):
# def get(self, request, pk):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# def put(self, request, pk):
#     serialize = BookSerializer(data=request.data)
#     serialize.is_valid(raise_exception=True)
#     serialize.validated_data()
#     serialize.save()
#     return Response('success', status=status.HTTP_201_CREATED)
#
# def delete(self, request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     book.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

# class BookDetails
# @api_view(['GET', 'PUT', 'DELETE'])
# def book_details(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("Details updated", status=status.HTTP_201_CREATED)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorViewSet(ModelViewSet):
    pagination_class = DefaultPagination
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filter_set_class = AuthorFilter


class BookViewSet(ModelViewSet):
    pagination_class = DefaultPagination
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]



# class AuthorDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
