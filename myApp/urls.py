#Este archivo servira para trabajar las urls desde myApp

#Imports utilizados
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#exportamos una lista nueva 
urlpatterns = [
    path('',views.Home, name='Home'),
    path('registro/', views.registro, name='registro'),
    path('Principal/', views.Principal, name='Principal'),
    path('logout', views.cerrar, name='logout'),
    path('Ingreso/', views.Ingreso, name='Ingreso'),
    path('procesar_formulario/', views.procesar_formulario, name='procesar_formulario'),
    path('Resolucion/', views.Resolucion, name='Resolucion'),
    path('updatePassword/', views.updatePassword, name='updatePassword'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)