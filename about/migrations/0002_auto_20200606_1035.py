# Generated by Django 3.0 on 2020-06-06 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='User_name',
            new_name='username',
        ),
    ]
