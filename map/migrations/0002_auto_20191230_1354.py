# Generated by Django 3.0.1 on 2019-12-30 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapmarks',
            name='comment',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='mapmarks',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
    ]
