# Generated by Django 4.2.6 on 2023-10-22 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
