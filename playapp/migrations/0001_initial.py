# Generated by Django 5.1.2 on 2024-11-03 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('progression', models.IntegerField()),
                ('idUser', models.CharField(max_length=200)),
                ('recompense', models.IntegerField()),
                ('key', models.CharField(max_length=200, unique=True)),
                ('Type', models.CharField(max_length=200)),
            ],
        ),
    ]