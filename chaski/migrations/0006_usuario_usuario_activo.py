# Generated by Django 4.0 on 2022-01-11 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chaski', '0005_remove_usuario_apellidos_remove_usuario_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='usuario_activo',
            field=models.BooleanField(default=True),
        ),
    ]