# Generated by Django 5.1.3 on 2024-11-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default_avatar.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='da', max_length=255),
        ),
    ]
