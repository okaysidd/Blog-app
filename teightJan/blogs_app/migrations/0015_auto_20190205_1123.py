# Generated by Django 2.1.4 on 2019-02-05 05:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0014_auto_20190204_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_model',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 5, 5, 53, 27, 97055, tzinfo=utc)),
        ),
    ]
