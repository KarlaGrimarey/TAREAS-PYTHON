# -*- coding: utf-8 -*-
"""GRUPO_6_TAREA1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IOxO6nDvJHq5WAw20mjUrwe4uZLhTchd
"""

#I. Utilizando un “if else” cree una estructura que evalúe “x” tal que:
# I. Utilizando un “if else” cree una estructura que evalúe “x” tal que:
# Si x es múltiplo de 2 imprima “Es múltiplo de 2”.
# Para otro caso, imprime “Otro caso”
# Muestra un ejemplo con x = 6.

x= int(input('Ingresa un numero entero:'))
if x%2 == 0:
   print("Es multiplo de 2")
else:
   print('Otro caso')

# Si x es múltiplo de 3 imprima “Es múltiplo de 3”
x= int(input('Ingresa tu un numero entero: '))
if x%3 == 0:
   print("Es multiplo de 3")
else:
  print('Otro caso')

# Si x es múltiplo de 2 y 3 imprima “Es múltiplo de 2 y 3”
x=int(input('Ingresa un numero entero:'))
if x%2== 0 and x%3==0:
  print('x es multiplo de 2 y 3')
else:
  print('Otro caso')

x= 6
if x%2== 0 and x%3==0:
  print('x es multiplo de 2 y 3')
if x%2==0:
  print('Es multiplo de 2')
if x%3==0:
  print('Es multiplo de 3')
else:
  print('Otro caso')

texto_2 = """II. Utilizando un “for loop” y el condicional “if else” para un rango del 1 al 100, evalúe “x” tal que: //
Si x es múltiplo de 3 imprima “Fizz”
Si x es múltiplo de 5 imprima “Buzz”
Si x es múltiplo de 3 y 5 imprima “FizzBuzz”
Para el resto de los casos, solo imprima el número """
print(texto_2)

x = list(range(1, 100))

for elemento in x:
  if elemento %3==0:
    print('Fizz')
  elif elemento %5==0:
    print('Buzz')
  elif elemento %3==0 and elemento %5==0:
    print('FizzBuzz')
  else:
    print(elemento)

texto_3 = """ III. Crea una función calcular_descuento() que permita calcular el descuento aplicado a un
producto. Si el total es mayor o igual a 1000, aplica un 20% de descuento, si el total es mayor
o igual a 500 pero menor a 1000, aplica un 10% de descuento. Si el total es menor a 500, no
aplica ningún descuento. La función debe devolver el total final después de aplicar el
descuento. Prueba la función con un total de compra de 1200, 750 y 300."""
print (texto_3)

def calcular_descuento(numero):
 if numero>= 1000:
  descuento= print(0.8 * numero)
 elif numero >= 500 and numero <= 1000:
  descuento= print(0.9* numero)
 elif numero < 500:
  descuento= numero
  return descuento

calcular_descuento(1200)

calcular_descuento(750)

calcular_descuento(300)

texto_4 = """IV. Crea una función llamada clasificar_edad() que reciba como parámetro la edad de una
persona. La función debe clasificar a la persona en una de las siguientes categorías:
"Niño" si la edad es menor de 12 años.
"Adolescente" si la edad está entre 12 y 17 años.
“Joven” si la edad está entre 18 y 24 años.
"Adulto" si la edad está entre 25 y 64 años.
"Adulto Mayor" si la edad es mayor o igual a 65 años.
La función debe devolver la categoría correspondiente. Prueba la función con las edades de
10, 19, 25 y 70. """
print (texto_4)

def clasificar_edad(edad):
 if edad<12:
  categoria= print('Niño')
 elif edad>=12 and edad<=17:
   categoria= print('Adolescente')
 elif edad>= 18 and edad<= 24:
  categoria= print ('Joven')
 elif edad>=25 and edad<=64:
  categoria= print('Adulto')
 elif edad>= 65:
  categoria= print('Adulto mayor')
  return categoria

clasificar_edad(10)

clasificar_edad(19)

clasificar_edad(25)

clasificar_edad(70)

texto_5 = """ V. Sea la fórmula del CRAEST PUCP

CRAEST = ((Media personal – media del curso)∗ 10)/Desviaciónestándar del curso + 50
Crea una función calcular_craest(media_personal,media_curso,desviacion_curso) que
reciba como tres únicos inputs tu media, la media del curso y la desviación estándar del curso
y te devuelva tu craest calculado. No te olvides documentar la función usando triple comillas
“”” """
print (texto_5)

def CRAEST(media_personal, media_curso, desviacion_curso):
  '''
    Objetivo:
        - Calcular el CRAEST de una persona dado su la media personal, media del curso y la desviacion estandar

    Input:
        - media_personal:         promedio personal en determinado curso
        - media_curso:            promedio general del curso
        - desviacion del curso:   variabilidad de las notas de los estudiantes respecto a la media

   Procedimiento:
        -Se calcula la diferencia entre la media personal y la media del curso: (media_neta)
        -Se le multiplica * 10 a la media neta
        -A la desviacion estandar se le suma 50
        -Se divide media_neta *10 sobre la desviacion estandar + 50

    Output:
        - CRAEST en el curso determinado
    '''
 media_neta = media_personal - media_curso
 craest= media_neta * 10 / desviacion_curso +50
 return craest

CRAEST(14,15,3.5)