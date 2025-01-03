# Generated by Django 5.1.2 on 2024-11-11 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playapp', '0004_ownertask_iduser_ownertask_progression_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dropbox_id', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('thumbnail_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
