# Generated by Django 4.2.2 on 2023-06-23 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_alter_perfil_imgperfil_alter_perfil_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='IMGPerfil',
            field=models.ImageField(blank=True, default='C:\\Users\\PC\\Documents\\Universidad\\Ciclo I 2023 UES\\Analisis numericos\\ANS-ProyectoFinal\\static/IMG/imagenPerfil.png', max_length=255, null=True, upload_to='Media/IMGPerfil', verbose_name='Imagen de perfil'),
        ),
    ]
