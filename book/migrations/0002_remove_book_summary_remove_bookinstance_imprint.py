# Generated by Django 4.2.1 on 2023-05-12 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='imprint',
        ),
    ]