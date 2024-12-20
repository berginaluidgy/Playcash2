# Generated by Django 5.1.2 on 2024-11-28 04:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playapp', '0009_userinfo_money_video_userid_alter_userinfo_userid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MissionVM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=0)),
                ('is_video_maker', models.BooleanField(default=False)),
                ('mission_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('total_videos', models.IntegerField(default=0)),
                ('completed_videos', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('completion_date', models.DateTimeField(blank=True, null=True)),
                ('progress', models.FloatField(default=0.0)),
                ('rewardMoney', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mission_vm', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
