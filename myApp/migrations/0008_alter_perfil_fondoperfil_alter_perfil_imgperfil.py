# Generated by Django 4.2.2 on 2023-06-23 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_alter_perfil_fondoperfil_alter_perfil_imgperfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='FondoPerfil',
            field=models.ImageField(blank=True, default='C:\\Users\\PC\\Documents\\Universidad\\Ciclo I 2023 UES\\Analisis numericos\\ANS-ProyectoFinal\\static/IMG/FondoPerfil.png', max_length=200, null=True, upload_to='Media/IMGFondo/', verbose_name='Fondo de perfil'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='IMGPerfil',
            field=models.ImageField(blank=True, default='C:\\Users\\PC\\Documents\\Universidad\\Ciclo I 2023 UES\\Analisis numericos\\ANS-ProyectoFinal\\static/IMG/imagenPerfil.png', max_length=255, null=True, upload_to='Media/IMGPerfil', verbose_name='Imagen de perfil'),
        ),
    ]
