# Generated by Django 3.0.1 on 2020-06-02 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20191230_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapmarks',
            name='id_comment',
            field=models.TextField(default=''),
        ),
    ]
