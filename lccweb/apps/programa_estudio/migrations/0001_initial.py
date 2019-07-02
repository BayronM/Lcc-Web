# Generated by Django 2.2.2 on 2019-07-02 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asignatura', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='programa_estudio',
            fields=[
                ('codigo', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('año', models.IntegerField(verbose_name=4)),
                ('semestre', models.IntegerField(verbose_name=1)),
                ('asig', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asignatura.asignatura')),
            ],
        ),
    ]
