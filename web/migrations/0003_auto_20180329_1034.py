# Generated by Django 2.0 on 2018-03-29 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='configuracionInicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgbanner1', models.CharField(choices=[('CONSTRUCCIÓN DE EDIFICACIONES', 'CONSTRUCCIÓN DE EDIFICACIONES'), ('CONSTRUCCIÓN', 'CONSTRUCCIÓN ')], max_length=1000, verbose_name='Imagen de Banner 1')),
                ('imgbanner2', models.CharField(choices=[('CONSTRUCCIÓN DE EDIFICACIONES', 'CONSTRUCCIÓN DE EDIFICACIONES'), ('CONSTRUCCIÓN', 'CONSTRUCCIÓN ')], max_length=1000, verbose_name='Imagen de Banner 2')),
                ('imgbanner3', models.CharField(choices=[('CONSTRUCCIÓN DE EDIFICACIONES', 'CONSTRUCCIÓN DE EDIFICACIONES'), ('CONSTRUCCIÓN', 'CONSTRUCCIÓN ')], max_length=1000, verbose_name='Imagen de Banner 3')),
                ('proyectoventa1', models.CharField(choices=[('CONSTRUCCIÓN DE EDIFICACIONES', 'CONSTRUCCIÓN DE EDIFICACIONES'), ('CONSTRUCCIÓN', 'CONSTRUCCIÓN ')], max_length=1000, verbose_name='Proyecto en venta 1')),
                ('proyectoventa2', models.CharField(choices=[('CONSTRUCCIÓN DE EDIFICACIONES', 'CONSTRUCCIÓN DE EDIFICACIONES'), ('CONSTRUCCIÓN', 'CONSTRUCCIÓN ')], max_length=1000, verbose_name='Proyecto en venta 2')),
                ('proyectoventa3', models.CharField(choices=[('CONSTRUCCIÓN DE EDIFICACIONES', 'CONSTRUCCIÓN DE EDIFICACIONES'), ('CONSTRUCCIÓN', 'CONSTRUCCIÓN ')], max_length=1000, verbose_name='Proyecto en venta 3')),
            ],
        ),
        migrations.DeleteModel(
            name='ImgInicio',
        ),
    ]
