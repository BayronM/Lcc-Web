# Generated by Django 2.2.2 on 2019-07-31 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignatura', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='requisito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codasig', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='asignatura',
            name='requisito',
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='req',
            field=models.ManyToManyField(to='asignatura.requisito'),
        ),
    ]
