# Generated by Django 2.0 on 2018-04-14 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0007_remove_contrato_valor_en_sm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contrato',
            old_name='valor_en_sm_participacion',
            new_name='valor_en_sm',
        ),
    ]
