# Generated by Django 4.2.6 on 2024-01-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='/books/default_book.png', upload_to=''),
        ),
    ]
