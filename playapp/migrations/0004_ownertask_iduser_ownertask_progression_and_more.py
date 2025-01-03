# Generated by Django 5.1.2 on 2024-11-03 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playapp', '0003_tiktokmission_ownertask_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownertask',
            name='idUser',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='ownertask',
            name='progression',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ownertask',
            name='recompense',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ownertask',
            name='status',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
