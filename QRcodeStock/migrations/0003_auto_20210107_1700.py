# Generated by Django 3.1.4 on 2021-01-07 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QRcodeStock', '0002_auto_20210107_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lote',
            old_name='id_usuario',
            new_name='id_usuario_criador',
        ),
    ]
