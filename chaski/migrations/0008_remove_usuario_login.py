# Generated by Django 4.0 on 2022-01-12 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chaski', '0007_rename_usuario_activo_usuario_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='login',
        ),
    ]
