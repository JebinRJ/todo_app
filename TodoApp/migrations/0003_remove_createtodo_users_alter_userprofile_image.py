# Generated by Django 4.1.4 on 2022-12-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0002_createtodo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createtodo',
            name='users',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to='getFile'),
        ),
    ]