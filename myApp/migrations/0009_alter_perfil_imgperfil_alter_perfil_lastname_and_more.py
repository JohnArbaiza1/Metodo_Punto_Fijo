# Generated by Django 4.2.2 on 2023-06-23 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_alter_perfil_fondoperfil_alter_perfil_imgperfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='IMGPerfil',
            field=models.ImageField(blank=True, default='IMG/imagenPerfil.png', max_length=255, null=True, upload_to='Media/IMGPerfil', verbose_name='Imagen de perfil'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='lastName',
            field=models.CharField(max_length=50, null=True, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Nombre'),
        ),
    ]
