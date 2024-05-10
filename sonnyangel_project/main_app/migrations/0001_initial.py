# Generated by Django 5.0.4 on 2024-05-01 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sonnyangel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=100)),
                ('sonnyangelname', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='images')),
            ],
        ),
    ]
