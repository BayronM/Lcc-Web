# Generated by Django 2.2.2 on 2019-07-16 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0007_prueba'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='nombre',
            field=models.CharField(choices=[('pep1', 'PEP 1'), ('pep2', 'PEP 2'), ('pep3', 'PEP 3'), ('recuperativa', 'Recuperativa'), ('examen', 'Examen')], default='pep1', max_length=7),
        ),
    ]
