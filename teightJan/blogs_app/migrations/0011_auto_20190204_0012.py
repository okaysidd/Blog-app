# Generated by Django 2.1.3 on 2019-02-03 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0010_auto_20190204_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_model',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
