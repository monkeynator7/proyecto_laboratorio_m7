# Generated by Django 4.2.2 on 2023-07-17 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0003_actualizando_campos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratorio',
            name='nombre',
            field=models.CharField(verbose_name='Nombre'),
        ),
    ]