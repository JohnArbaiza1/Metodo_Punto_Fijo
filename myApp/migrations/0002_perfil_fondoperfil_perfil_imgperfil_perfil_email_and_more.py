# Generated by Django 4.2.2 on 2023-06-23 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='FondoPerfil',
            field=models.ImageField(blank=True, default='static/IMG/FondoPerfil.png', max_length=200, null=True, upload_to='Media/IMGFondo', verbose_name='Fondo de perfil'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='IMGPerfil',
            field=models.ImageField(blank=True, default='static/IMG/imagenPerfil.png', max_length=255, null=True, upload_to='Media/IMGPerfil', verbose_name='Imagen de perfil'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, verbose_name='Correo electrónico'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='lastName',
            field=models.CharField(blank=True, max_length=50, verbose_name='Apellido'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL),
        ),
    ]
