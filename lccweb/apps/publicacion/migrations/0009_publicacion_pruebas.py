# Generated by Django 2.2.2 on 2019-07-16 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0008_prueba_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='pruebas',
            field=models.ManyToManyField(to='publicacion.prueba'),
        ),
    ]
