

"""
Created on Tue May 25 16:37:23 2021

@author: oscar
"""

'''
===============================================================================

Programa para conversion de temperatura.

===============================================================================

Las tres escalas de temperatura más comunes son: Celsius, Fahrenheit y Kelvin.

Una escala de temperatura puede ser creada identificando dos temperaturas
fácilmente reproducibles. Las temperaturas de ebullición (cambio de estado
líquido a vapor) y de fusión (cambio del estado sólido al líquido) del agua, a
una atmósfera de presión, son ejemplos de parámetros utilizados.

La escala Celsius (°C) toma en cuenta el valor °0, para el punto de fusión del
agua, mientras que el punto de ebullición del agua corresponde a 100°. En el
caso de la escala Fahrenheit (°F), el punto de fusión del agua está a los 32°,
y el de ebullición a los 212°. Es muy importante recordar que la variación en
temperatura de un grado Celsius es mayor a la variación en temperatura de un
grado Fahrenheit. Solo 100° C cubren el mismo rango que 180° F.

La escala Kelvin (abreviada como K, sin el símbolo de grado) es la escala más
común utilizada para el trabajo científico, por una serie de características,
como por ejemplo, que su 0 es el cero absoluto, es decir, la temperatura en la
que los átomos y moléculas presentan la menor energía térmica posible. En esta
escala, el punto de fusión del agua se da a los 273 K, y el de ebullición, a
los 373 K. Como puedes notar, la magnitud de las diferencias de temperatura es
la misma en Celsius y en Kelvin, es decir, la variación de un grado en la
escala Celsius corresponde también a una variación de un grado en la escala
Kelvin.

La termodinamica nos da las ecuaciones para la conversion de temperatura.

*******************************************************************************

Conversion de Celsius a Fahrenheit:

    T(°F) = [9/5 * T(°C)] + 32

*******************************************************************************

Conversion de Fahrenheit a Celcius:

    T(°C) = 5/9 * [T(°F) - 32]

*******************************************************************************

Conversion de Celsius a Kelvin:

    T(K) = T(°C) + 273

*******************************************************************************

Conversion de Kelvin a Celsius:

    T(°C) = T(K) - 273

*******************************************************************************

Conversion de Fahrenheit a Kelvin:

    T(k) = [5/9 * (T(°F) - 32)] + 273

*******************************************************************************

Conversion de Kelvin a Fahrenheit:

    T(°F) = [9/5 * (T(k) - 273)] + 32

*******************************************************************************

Si el usuario ingresa un valor de temperatura menor al CERO ABSOLUTO el
programa muestra un aviso por pantalla y termina.

Para mas informacion ver:

https://es.khanacademy.org/science/fisica-pe-pre-u/x4594717deeb98bd3:energia-cinetica/x4594717deeb98bd3:calor-y-temperatura/a/643-escalas-de-temperatura

'''

import sys

print('\n\n')
print("-"*80)
print('Programa para conversion de temperatura')
print('Autor: Oscar Lancheros')
print("-"*80)
print('\nSeleccione una de las siguientes opciones:\n')
print('Para convertir de Celsius a Fahrenheit digite 1')
print('Para convertir de Fahrenheit a Celsius digite 2')
print('Para convertir de Celsius a Kelvin digite 3')
print('Para convertir de Kelvin a Celsius digite 4')
print('Para convertir de Fahrenheit a Kelvin digite 5')
print('Para convertir de Kelvin a Fahrenheit digite 6\n')
print("-"*80)
print('\n')

select = input('Digite el tipo de conversion de temperatura que desea hacer: ')
print('\n')

opciones = ['1', '2', '3', '4', '5', '6']

try:
    if select not in opciones:
        print("-"*80)
        print('Eleccion no valida, por favor intente de nuevo')
        print("-"*80)
except:
    exit()

###############################################################################
#Fahrenheit to Celsius
#Far2Cel = 9/5 * Cel + 32.0
###############################################################################

if select == '1':
    Cel = input('Ingrese la temperatura en °C para convertir a °F: ')
    print('\n')
    Cel = float(Cel)
    
    if Cel < -273.15:
        print('ERROR')
        print('Esa temperatura viola el Segundo Principio de la Termodinamica')
        sys.exit()
    
    else:
        Far2Cel = 9/5 * Cel + 32.0
        Far2Cel = round(Far2Cel, 1)
        print(Cel, '°C =', Far2Cel,'°F')
        print('\n\n')

###############################################################################
#Celsius to Fahrenheit
#Cel2Far = 5/9 * (Far - 32.0)
###############################################################################

elif select == '2':
    Far = input('Ingrese la temperatura en °F para convertir a °C: ')
    print('\n')
    Far = float(Far)
    
    if Far < -459.67:
        print('ERROR')
        print('Esa temperatura viola el Segundo Principio de la Termodinamica')
        sys.exit()
    
    else:
        Cel2Far = 5/9 * (Far - 32.0)
        Cel2Far = round(Cel2Far, 1)
        print(Far,'°F = ', Cel2Far, '°C')
        print('\n\n')

###############################################################################
#Celsius to Kelvin
#Cel2Kel = Cel + 273.0
###############################################################################

elif select == '3':
    Cel = input('Ingrese la temperatura en °C para convertir a K: ')
    print('\n')
    Cel = float(Cel)
    
    if Cel < -273.15:
        print('ERROR')
        print('Esa temperatura viola el Segundo Principio de la Termodinamica')
        sys.exit()
        
    else:
        Cel2Kel = Cel + 273.0
        Cel2Kel = round(Cel2Kel, 1)
        print(Cel, '°C = ', Cel2Kel, 'K')
        print('\n\n')

###############################################################################
#Kelvin to Celsius
#Kel2Cel = Kel - 273.0
###############################################################################

elif select == '4':
    Kel = input('Ingrese la temperatura en K para convertir a °C: ')
    print('\n')
    Kel = float(Kel)
    
    if Kel < 0.0:
        print('ERROR')
        print('Esa temperatura viola el Segundo Principio de la Termodinamica')
        sys.exit()
        
    else:
        Kel2Cel = Kel - 273.0
        Kel2Cel = round(Kel2Cel, 1)
        print(Kel, 'K = ', Kel2Cel, '°C')
        print('\n\n')

###############################################################################
#Fahrenheit to Kelvin
#Far2Kel = (5/9 * (Far - 32.0)) + 273.0
###############################################################################

elif select == '5':
    Far = input('Ingrese la temperatura en °F para convertir a K: ')
    print('\n')
    Far = float(Far)
    
    if Far < -459.67:
        print('ERROR')
        print('Esa temperatura viola el Segundo Principio de la Termodinamica')
        sys.exit()
    
    else:
        Far2Kel = (5/9 * (Far - 32.0)) + 273.0
        Far2Kel = round(Far2Kel, 1)
        print(Far,'°F = ',Far2Kel, 'K')
        print('\n\n')

###############################################################################
#Kelvin to Fahrenheit
#Kel2Far = (9/5 * (Kel - 273)) + 32.0
###############################################################################

elif select == '6':
    Kel = input('Ingrese la temperatura en K para convertir a °F: ')
    print('\n')
    Kel = float(Kel)
    
    if Kel < 0.0:
        print('ERROR')
        print('Esa temperatura viola el Segundo Principio de la Termodinamica')
        sys.exit()
    
    else:
        Kel2Far = (9/5 * (Kel - 273)) + 32.0
        Kel2Far = round(Kel2Far, 1)
        print(Kel, 'K = ', Kel2Far, '°F')

#End of program
