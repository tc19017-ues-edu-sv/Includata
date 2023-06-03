# Generated by Django 4.2.1 on 2023-06-03 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0004_ragoedades'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriaocupacional',
            name='detalle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Dashboard.detalleestadisticodiscapacitado'),
        ),
        migrations.AddField(
            model_name='ragoedades',
            name='detalle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Dashboard.detalleestadisticodiscapacitado'),
        ),
        migrations.AddField(
            model_name='rubro',
            name='detalle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Dashboard.detalleestadisticodiscapacitado'),
        ),
    ]