# Generated by Django 2.1.4 on 2019-02-13 11:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0021_auto_20190213_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_model',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 13, 11, 43, 46, 663700, tzinfo=utc)),
        ),
    ]
