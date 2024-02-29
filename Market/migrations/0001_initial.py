# Generated by Django 4.2.2 on 2024-02-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=80)),
                ('comments', models.TextField(max_length=500)),
            ],
        ),
    ]