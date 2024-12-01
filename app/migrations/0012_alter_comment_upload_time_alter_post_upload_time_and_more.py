# Generated by Django 5.1.3 on 2024-11-30 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_comment_upload_date_alter_comment_upload_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='upload_time',
            field=models.TimeField(blank=True, default=datetime.time(12, 34, 28, 90401)),
        ),
        migrations.AlterField(
            model_name='post',
            name='upload_time',
            field=models.TimeField(blank=True, default=datetime.time(12, 34, 28, 90128)),
        ),
        migrations.AlterField(
            model_name='user',
            name='creation_time',
            field=models.TimeField(blank=True, default=datetime.time(12, 34, 28, 89841)),
        ),
    ]