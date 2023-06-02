# Generated by Django 4.2.1 on 2023-06-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoriaOcupacional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCategoria', models.IntegerField()),
                ('nombreCategoria', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='rubro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idRubro', models.IntegerField()),
                ('nombreRubro', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='sectorEconomico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idSector', models.IntegerField()),
                ('nombreSector', models.CharField(max_length=30)),
            ],
        ),
    ]
