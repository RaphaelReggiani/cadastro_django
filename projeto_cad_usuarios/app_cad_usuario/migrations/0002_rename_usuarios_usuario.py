# Generated by Django 5.0.4 on 2024-04-15 19:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app_cad_usuario", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Usuarios",
            new_name="Usuario",
        ),
    ]
