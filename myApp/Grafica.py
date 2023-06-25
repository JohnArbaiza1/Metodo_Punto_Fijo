from sympy import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import base64
import io
from io import BytesIO

class grafica:
    
    def grafico(expresion, number):
        x = symbols('x')
        ecuacion = simplify(expresion)
        numero= np.linspace(-20,20,100)
        plt.figure()
        plt.plot(numero, [ecuacion.evalf(subs={x:i}) for i in numero])
        plt.plot(number, ecuacion.evalf(subs={x:number}), marker="o")
        plt.annotate(str(number), (number, ecuacion.evalf(subs={x:number})))
        plt.grid()
        plt.xlim(-15, 15)
        plt.ylim(-15, 15)
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")
        plt.title(label="Punto Fijo")
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        #codificamos la imagen
        image64 = base64.b64encode(buffer.getvalue()).decode()
        return image64
    def Verificar(funcion, valor):
        x = symbols("x")
        obtenido = funcion.evalf(subs={x:valor})
        if float(obtenido) >= 0.0 and float(obtenido)<=1.0:
            return 1
        else:
            return 2
    def verificandoGx(ec):
        x = symbols("x")
        derivada = diff(ec, x)
        return derivada
    
    def Proceso(expresion,X0,E):

        #Definimos listas vacias para almacenar los resultados que se se obtengan
        iteraciones = []
        Valor_Xi = []
        Valor = []
        Error_Calc = []

        #Definimos un simbolo haciendo uso de las funciones de la libreria sympy
        x = symbols('x')

        #Nos ayudara a evaluar la expresion
        fx = lambdify(x,expresion)
        #Establecemos un contador que guarde el numero de iteraciones hechas
        contador = 0
        #salida = True
        #Hacemos uso del ciclo while para hacer las operaciones de cada itecion
        while True:
            Xi = fx(X0)
            #Formula para calcular el punto fijo
            producto = abs((Xi - X0) / Xi)

            #Formula para calcular el % de error
            porcetaje = (abs((Xi - X0) / Xi)) * 100

            #Agregando los valores de las iteraciones a las listas vacias 
            iteraciones.append(contador+1)
            Valor_Xi.append(Xi)
            #nuevo vector creado
            Valor.append(X0)
            Error_Calc.append(porcetaje)

            #Verificamos si lo que se encuentra en producto es menor que el error
            if producto < E:
                break
            #Actualizamos el valor para la proxima iteracion
            X0 = Xi
            #Incrementamos el contador
            contador += 1
        return Xi
    
    def Iteraciones(expresion,X0,E):

        #Definimos listas vacias para almacenar los resultados que se se obtengan
        iteraciones = []
        Valor_Xi = []
        Valor = []
        Error_Calc = []

        #Definimos un simbolo haciendo uso de las funciones de la libreria sympy
        x = symbols('x')

        #Nos ayudara a evaluar la expresion
        fx = lambdify(x,expresion)
        #Establecemos un contador que guarde el numero de iteraciones hechas
        contador = 0
        #salida = True
        #Hacemos uso del ciclo while para hacer las operaciones de cada itecion
        while True:
            Xi = fx(X0)
            #Formula para calcular el punto fijo
            producto = abs((Xi - X0) / Xi)

            #Formula para calcular el % de error
            porcetaje = (abs((Xi - X0) / Xi)) * 100

            #Agregando los valores de las iteraciones a las listas vacias 
            iteraciones.append(contador+1)
            Valor_Xi.append(Xi)
            #nuevo vector creado
            Valor.append(X0)
            Error_Calc.append(porcetaje)

            #Verificamos si lo que se encuentra en producto es menor que el error
            if producto < E:
                break
            #Actualizamos el valor para la proxima iteracion
            X0 = Xi
            #Incrementamos el contador
            contador += 1
            #Data frame que servira como tabla para mostar los valores obtenidos
        dataFrame = {'i': iteraciones,'X':Valor, 'Xi+1':Valor_Xi, 'E':Error_Calc, 'Signo':'<', 'Error':E}
        df = pd.DataFrame(dataFrame)
        return df