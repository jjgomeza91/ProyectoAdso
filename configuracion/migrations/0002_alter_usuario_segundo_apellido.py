# Generated by Django 4.2.7 on 2023-11-10 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='segundo_apellido',
            field=models.CharField(max_length=45, verbose_name='Segundo Apellido'),
        ),
    ]
