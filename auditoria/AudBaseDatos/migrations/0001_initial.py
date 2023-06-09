# Generated by Django 4.0.4 on 2022-05-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TableName', models.CharField(max_length=100, verbose_name='Nombre Tabla')),
                ('Operation', models.CharField(max_length=1, verbose_name='Operación')),
                ('OldValue', models.CharField(blank=True, max_length=255, verbose_name='Antiguos valores')),
                ('NewValue', models.CharField(blank=True, max_length=255, verbose_name='Nuevos valores')),
                ('UpdateDate', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('UserName', models.CharField(max_length=70, verbose_name='Usuario')),
                ('idtabla', models.CharField(max_length=70, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Ubicacion',
                'verbose_name_plural': 'Ubicaciones',
            },
        ),
    ]
