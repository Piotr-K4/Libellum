# Generated by Django 4.2.6 on 2024-01-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_realease',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='source',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]