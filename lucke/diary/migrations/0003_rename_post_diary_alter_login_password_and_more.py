# Generated by Django 5.0.6 on 2024-06-30 09:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_login'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Diary',
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
