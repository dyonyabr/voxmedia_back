# Generated by Django 5.1.3 on 2024-11-29 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_post_title_post_content_post_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
