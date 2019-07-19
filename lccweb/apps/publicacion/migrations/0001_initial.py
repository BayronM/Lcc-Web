# Generated by Django 2.2.2 on 2019-07-18 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seccion', '0002_remove_seccion_admin'),
        ('asignatura', '0002_remove_asignatura_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='publicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=30)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/')),
                ('fecha', models.DateField()),
                ('calendarioprueba', models.IntegerField(choices=[(1, 'Si'), (0, 'No')], default=0)),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seccion.seccion')),
            ],
        ),
        migrations.CreateModel(
            name='noticia',
            fields=[
                ('publicacion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='publicacion.publicacion')),
                ('descripcion', models.TextField()),
                ('cuerpo', models.TextField()),
            ],
            bases=('publicacion.publicacion',),
        ),
        migrations.CreateModel(
            name='prueba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('pep1', 'PEP 1'), ('pep2', 'PEP 2'), ('pep3', 'PEP 3'), ('recuperativa', 'Recuperativa'), ('examen', 'Examen')], default='pep1', max_length=7)),
                ('fecha', models.DateField()),
                ('horario', models.CharField(choices=[('1', 'Modulo 1-2 (8:00-9:30)'), ('2', 'Modulo 3-4 (9:40-11:10)'), ('3', 'Modulo 5-6 (11:20-12:50)'), ('4', 'Modulo 7-8 (13:50-15:20)'), ('5', 'Modulo 9-10 (15:30-17:00)'), ('6', 'Modulo 11-12 (17:10-18:40)'), ('7', 'Modulo 13-14 (18:45-20:10)'), ('8', 'Modulo 15-16 (20:10-21:35)'), ('9', 'Modulo 17-18 (21:35-23:00)'), ('0', 'Horario sin asignar')], default='0', max_length=6)),
                ('semestre', models.CharField(choices=[('1', 'Primer semestre'), ('2', 'Segundo semestre')], default='1', max_length=1)),
                ('sala', models.CharField(max_length=10)),
                ('asig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asignatura.asignatura')),
            ],
        ),
    ]
