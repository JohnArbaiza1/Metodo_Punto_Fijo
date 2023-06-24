#------------------------------------------------------------------
from django.shortcuts import render,redirect

#para crear formularios de registro y comprobar que el usuario existe
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

#Para el registro de usuarios
from django.contrib.auth.models import User

#Para crear cookies
from django.contrib.auth import login, logout, authenticate

#import para la respuesta HTTP
from django.http import HttpResponse

#Para los errores de integrida en la base de datos
from django.db import IntegrityError

#Import de la clase perfil
from .models import Perfil

#Import de la clase forms que se creo
from .forms import *
#-------------------------------------------------------------------
# Create your views here.

def Home(request):
    return render(request, 'index.html')

#Funcion que ayuda con el registro de usuarios
def registro(request):

    #Indicando que si nos visitan con get vamos a retornar el form
    if request.method == 'GET':
        return render(request, 'Registro.html',{
        'form': UserCreationForm
    })

    #Indicando que si nos visistan por medio de post se debe comparar que los password sean correctos
    else:
        # Verificando que no existan campos vacíos
        required_fields = ['username', 'password1', 'password2']
        for field in required_fields:
            if not request.POST.get(field):
                return render(request, 'Registro.html', {
                    'form': UserCreationForm,
                    'error': 'Por favor, complete todos los campos'
                })
            
        if request.POST['password1'] == request.POST['password2']:
          try:
              #registrando usuario en caso de que las password coincidan
              user =  User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])

              #guardando el usuario dentro de la base de datos
              user.save()
              login(request, user)
              #Rederigimos a la pagina principal
              return redirect('Principal')
          
          except IntegrityError:
                   return render(request, 'Registro.html',{
                       'form': UserCreationForm,
                       'error': 'Este usuario ya existe'
                      })
          
        return render(request, 'Registro.html',{
                       'form': UserCreationForm,
                       'error': 'passwords do not match'
                      })
        

def Principal(request):
    profile = Perfil.objects.get(user=request.user)

    if request.method == 'POST':
         # Si la solicitud es POST, se intenta guardar el formulario enviado
          form = PerfilForm(request.POST, request.FILES, instance=profile)
          if form.is_valid():
              form.save()
              return redirect('Principal') 
    else:
        # Si la solicitud es GET, se muestra el formulario vacío o prellenado con los datos existentes
        form = PerfilForm(instance=profile)

    return render(request, 'Principal.html', {'perfil': profile, 'form': form})

def cerrar(request):
    logout(request)
    return redirect('Home')

#Funcion del login
def Ingreso(request):
    #Si el metodo es get se envia el formulario
    if request.method == 'GET':
          return render(request, 'Login.html',{
            'form': AuthenticationForm
           })
    else:
        #comprobando si los datos que se estan ingresando son validos
        user =  authenticate(request, username=request.POST['username'], password=request.POST['password'])

        #Comprobando si el usuario es valido de no ser asi se le muestra un mensaje
        if user is None:
            return render(request, 'Login.html',{
            'form':AuthenticationForm,
            'Error': 'Usuario o contraseña incorrectos'
           })
        #si el usuario existe se manda a principal
        else:
            #Guardando la sesión
            login(request, user)
            return redirect('Principal')
        



  

