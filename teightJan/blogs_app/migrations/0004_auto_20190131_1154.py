# Generated by Django 2.1.4 on 2019-01-31 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0003_auto_20190129_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment_model',
            old_name='comment',
            new_name='comment_text',
        ),
    ]
