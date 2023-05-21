from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)


class Author(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=True, null=False)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"The author's name is {self.first_name} {self.last_name}, born on {self.date_of_birth}."


class Book(models.Model):
    LANGUAGE_CHOICES = [
        ("ENGLISH", "ENGLISH"),
        ("YORUBA", "YORUBA"),
        ("IGBO", "IGBO"),
        ("HAUSA", "HAUSA")
    ]

    GENRE_CHOICES = [
        ('FICTION', 'FICTION'),
        ('POLITICS', 'POLITICS'),
        ('FINANCE', 'FINANCE'),
        ('ROMANCE', 'ROMANCE')
    ]

    title = models.CharField(max_length=100, blank=False, null=False)
    isbn = models.CharField(max_length=13, blank=False, null=False)
    description = models.CharField(max_length=300, blank=False, null=False)
    date_added = models.DateTimeField(blank=True, null=True)
    genre = models.CharField(max_length=15, choices=GENRE_CHOICES)
    language = models.CharField(max_length=15, choices=LANGUAGE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return f"The book titled {self.title} was written by {self.author}" \
               f"Its was added on {self.date_added}" \
               f"Written in {self.language} language" \
               f"The genre is {self.genre}," \
               f"It costs {self.price}" \
               f"The isbn is {self.isbn}"


class BookInstance(models.Model):
    STATUS_CHOICES = [('AVAILABLE', 'A'),
                      ('BORROWED', 'B')]
    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    due_back = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"The book {self.book} status is {self.status}"
