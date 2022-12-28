# Generated by Django 4.1.4 on 2022-12-26 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TodoApp', '0004_createtodo_date_alter_createtodo_todo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='createtodo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
