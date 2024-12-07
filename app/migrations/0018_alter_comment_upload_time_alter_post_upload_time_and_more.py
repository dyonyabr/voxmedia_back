# Generated by Django 5.1.3 on 2024-12-06 14:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_comment_upload_date_alter_comment_upload_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='upload_time',
            field=models.TimeField(blank=True, default=datetime.time(17, 53, 39, 905465)),
        ),
        migrations.AlterField(
            model_name='post',
            name='upload_time',
            field=models.TimeField(blank=True, default=datetime.time(17, 53, 39, 905191)),
        ),
        migrations.AlterField(
            model_name='user',
            name='creation_time',
            field=models.TimeField(blank=True, default=datetime.time(17, 53, 39, 904905)),
        ),
    ]