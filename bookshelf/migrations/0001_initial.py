# Generated by Django 3.2.9 on 2021-11-16 18:20

import bookshelf.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.CharField(default=bookshelf.models.random_book_cover, max_length=2)),
                ('title', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=50, null=True)),
                ('borrow', models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 16, 19, 20, 27, 371479))),
            ],
        ),
    ]
