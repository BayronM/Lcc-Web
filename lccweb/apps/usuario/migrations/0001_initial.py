<<<<<<< HEAD
# Generated by Django 2.2.3 on 2019-07-19 22:00
=======
# Generated by Django 2.2.2 on 2019-07-20 02:54
>>>>>>> 41c7a51da919e2ff91798948bdeb328514ec0dd1

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('codigo', models.CharField(max_length=10)),
                ('rut', models.IntegerField()),
                ('nombre', models.CharField(max_length=20)),
                ('paterno', models.CharField(max_length=20)),
                ('materno', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('contraseña', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='administrador',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuario.usuario')),
                ('email2', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=10)),
            ],
            bases=('usuario.usuario',),
        ),
        migrations.CreateModel(
            name='estudiante',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuario.usuario')),
                ('nivel', models.IntegerField()),
                ('agnoing', models.DateField()),
            ],
            bases=('usuario.usuario',),
        ),
    ]
