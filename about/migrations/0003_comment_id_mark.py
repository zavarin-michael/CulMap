# Generated by Django 3.0.1 on 2020-06-06 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20200606_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='id_mark',
            field=models.IntegerField(default='-1'),
        ),
    ]
