from django.db import models
import os
from django.conf import settings


#Imports a emplear

#importanto la tabla de usuarios
from django.contrib.auth.models import User

#import para poder hacer usuo de las señales
from django.db.models.signals import post_save

# Create your models here.


#Creando la tabla para perfil del usuario
class Perfil(models.Model):
    #Camplos de la tabla y relacion con la tabla de usuarios
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil', default=1)
    email = models.EmailField('Correo electrónico', max_length=200, blank=True, null=True)
    name = models.CharField(max_length=50, verbose_name='Nombre', null=True)
    lastName = models.CharField(max_length=50, verbose_name='Apellido', null=True)
    IMGPerfil = models.ImageField('Imagen de perfil', default= 'static/IMG/imagenPerfil.png', upload_to='Media/IMGPerfil', max_length=255)
    FondoPerfil = models.ImageField('Fondo de perfil', default='static/IMG/FondoPerfil.png', upload_to='Media/IMGFondo/', max_length=200)
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']


#Funcion para crear el perfil
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

#Funcion para grabar los datos del usuario
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()

#Señales para crear perfil y que se grabe
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)