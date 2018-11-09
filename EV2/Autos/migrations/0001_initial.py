# Generated by Django 2.1.3 on 2018-11-09 11:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automovil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('Marca', models.CharField(max_length=200)),
                ('Modelo', models.CharField(max_length=200)),
                ('Año_automovil', models.DateTimeField(default=django.utils.timezone.now)),
                ('Color', models.CharField(max_length=200)),
                ('Numero_puertas', models.CharField(max_length=200)),
                ('Descripcion', models.TextField()),
                ('Fecha_publicacion', models.DateTimeField(blank=True, null=True)),
                ('Precio', models.CharField(max_length=200)),
            ],
        ),
    ]