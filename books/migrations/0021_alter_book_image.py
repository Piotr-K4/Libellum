# Generated by Django 4.2.6 on 2024-01-26 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0020_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='default_book.png', upload_to='books/'),
        ),
    ]
