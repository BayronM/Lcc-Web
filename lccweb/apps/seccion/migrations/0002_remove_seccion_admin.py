# Generated by Django 2.2.2 on 2019-07-16 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seccion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seccion',
            name='admin',
        ),
    ]
