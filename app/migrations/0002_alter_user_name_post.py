# Generated by Django 5.1.3 on 2024-11-29 08:19

import django.db.models.deletion
from django.db import migrations, models

def populate_content(apps, schema_editor):
    Post = apps.get_model('app', 'Post')
    for post in Post.objects.all():
        post.content = "Default content"
        post.save()

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.RunPython(populate_content),
    ]