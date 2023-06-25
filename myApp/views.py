#------------------------------------------------------------------
from django.shortcuts import render,redirect

#para crear formularios de registro y comprobar que el usuario existe
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

#Para el registro de usuarios
from django.contrib.auth.models import User

#Para crear cookies
from django.contrib.auth import login, logout, authenticate,get_user_model

#Para mostrar mensajes 
from django.contrib import messages

#import para la respuesta HTTP
from django.http import HttpResponse

#Para los errores de integrida en la base de datos
from django.db import IntegrityError

#Import de la clase perfil
from .models import Perfil

#Import de la clase forms que se creo
from .forms import *

#importacion de procesos
from .Grafica import*

# Create your views here.

#-------------------------------------------------------------------------------------------

def info(request):
    return render(request, 'Info.html')

#-------------------------------------------------------------------------------------------

def Home(request):
    return render(request, 'index.html')

#-------------------------------------------------------------------------------------------

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
                       'error': 'las contraseñas no coinciden'
                      })

#-------------------------------------------------------------------------------------------
        
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

#-------------------------------------------------------------------------------------------

def cerrar(request):
    logout(request)
    return redirect('Home')

#-------------------------------------------------------------------------------------------

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
#-------------------------------------------------------------------------------------------

#Para obtener el usuario 
User = get_user_model()
        
#Funcion que se encarga de la actualizacion de la contraseña 
def updatePassword(request):
      #Verificamos si la solicitud es post
    if request.method == 'POST':
        #Se obtienen los datos del formulario
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Verificando que no existan campos vacíos
        if not username or not password1 or not password2:
            messages.error(request, 'Por favor, ingrese todo los datos requeridos')
            return redirect('updatePassword')
        
        try:
            #Se encarga de buscar y obtener al usuario ingresado
            user = User.objects.get(username=username)

             #Verificando que las password coincidan
            if password1 != password2:
                #Mensaje que se muestra en caso de que las password no sean iguales
                messages.error(request, 'Las contraseñas no coinciden.')
                return redirect('updatePassword')
            
            #Estableciendo la nueva password para el usuario que lo solicita
            user.set_password(password1)
            user.save()
            #Mensaje que se muestra al actualizar la password
            messages.success(request, 'Contraseña actualizada exitosamente')
            #Rederigimos a la pagina de inicio
            return redirect('Ingreso')
        
        except User.DoesNotExist:
            #Mensaje que se muestra en caso de que el usuario no exista
            messages.error(request, 'El usuario ingresado no existe intente de nuevo')
            return redirect('updatePassword')
        
    return render(request, 'NewPassword.html')

#-------------------------------------------------------------------------------------------
            
def procesar_formulario(request):
    if request.method == 'POST':
        #funcion principal que sirve para graficar
        funcion = request.POST.get('funcion')
        #funcion despejada que sera para verificar si es buena g(x)
        funcion2 = request.POST.get('funcion2')
        #mandamos a derivar la ecuacion para verificar si es buena g(x)
        deriva = grafica.verificandoGx(funcion2)
        #obtenemos el valor inicial
        valor_inicial = float(request.POST.get('Valor'))
        #obtenemos el dato para verificar si es buena g(x)
        dato = grafica.Verificar(deriva, valor_inicial)
        #obtenemos el margen de error
        margen_error = float(request.POST.get('error'))
        #procesamos para encontrar la raiz
        raiz = grafica.Proceso(funcion2, valor_inicial, margen_error)
        imagen = grafica.grafico(funcion, raiz)
        arrayV = np.array([funcion, funcion2, valor_inicial, margen_error, raiz])
        data = grafica.Iteraciones(funcion2, valor_inicial, margen_error)
        iteraciones_html= data.to_html()
        iteraciones_html = iteraciones_html.replace('<table', '<table class="table table-bordered"')
        return render(request, 'Resolucion.html ',{
            'numeros': arrayV,
            'imagen': imagen,
            'iteraciones': iteraciones_html,
        })
    
def Resolucion(request):
    return render(request,'Resolucion.html')

def procesar_formulario_User(request):
    if request.method == 'POST':
        #funcion principal que sirve para graficar
        funcion = request.POST.get('funcion')
        #funcion despejada que sera para verificar si es buena g(x)
        funcion2 = request.POST.get('funcion2')
        #mandamos a derivar la ecuacion para verificar si es buena g(x)
        deriva = grafica.verificandoGx(funcion2)
        
        #obtenemos el valor inicial
        valor_inicial = float(request.POST.get('Valor'))
        #obtenemos el dato para verificar si es buena g(x)
        dato = grafica.Verificar(deriva, valor_inicial)
        #obtenemos el margen de error
        margen_error = float(request.POST.get('error'))

        #procesamos para encontrar la raiz
        raiz = grafica.Proceso(funcion2, valor_inicial, margen_error)
        imagen = grafica.grafico(funcion, raiz)
        arrayV = np.array([funcion, funcion2, valor_inicial, margen_error, raiz])
        data = grafica.Iteraciones(funcion2, valor_inicial, margen_error)
        iteraciones_html= data.to_html()
        iteraciones_html = iteraciones_html.replace('<table', '<table class="table table-bordered"')
        return render(request, 'Resolucion2.html ',{
            'numeros': arrayV,
            'imagen': imagen,
            'iteraciones': iteraciones_html
        })
    
def Resolucion_User(request):
    return render(request,'Resolucion2.html')