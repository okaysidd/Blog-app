# Generated by Django 2.1.4 on 2019-02-08 12:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0018_auto_20190208_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_model',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 12, 14, 27, 469648, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post_model',
            name='liked_by',
            field=models.ManyToManyField(blank=True, default=[], null=True, related_name='liked_by', to='users_app.Author_model'),
        ),
    ]