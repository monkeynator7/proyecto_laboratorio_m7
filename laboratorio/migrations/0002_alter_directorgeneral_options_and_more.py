# Generated by Django 4.2.2 on 2023-07-11 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directorgeneral',
            options={'verbose_name': 'Director General', 'verbose_name_plural': 'Directores Generales'},
        ),
        migrations.AlterModelTable(
            name='directorgeneral',
            table='Director General',
        ),
    ]
