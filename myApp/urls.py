#Este archivo servira para trabajar las urls desde myApp

#Imports utilizados
from django.urls import path
from . import views

#exportamos una lista nueva 
urlpatterns = [
    path('',views.Home, name='Home'),
    path('registro/', views.registro, name='registro'),
    path('Principal/', views.Principal, name='Principal'),
    path('logout', views.cerrar, name='logout'),
    path('Ingreso/', views.Ingreso, name='Ingreso'),
]