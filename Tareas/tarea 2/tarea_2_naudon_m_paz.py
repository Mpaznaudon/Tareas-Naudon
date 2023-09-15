# -*- coding: utf-8 -*-
"""Tarea 2 Naudon M Paz

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W36ntt0aa4VZxlJLDxdNS6qGGLVvfDYG
"""

# calcular la nota final de un estudiante teniedo en cuenta que L
# la primera nota vale 30% de la nota final
# la segunda nota vale 30% de la nota final
# y el trabajo final vale 40% de la nota final

nota_1 =  float(input("ingresa nota1"))
nota_2 = float(input("ingresa nota2"))
nota_3 = float(input("ingresa nota3"))
ponderación = nota_1*0.3 + nota_2*0.3 + nota_3*0.4

print(ponderación)

if (ponderación>=4):
  print("APROBASTE!")
elif (ponderación<4):
  print("REPROBASTE")
else:
  print("ERROR")

"""1. Hacer un programa que imprima los números del 1 al 100, en python sería:"""

#comentario: importante print por o si no, no transcribe los codigos

print (range(100))

for x in range(100):
  print(x+1)

"""
2. **Hacer un programa que imprima los números del 1 al 100 que sean divisibles entre 3 (con resto 0)**
Esto signifca que si el número es 3, 6, 9, 12, 15, etc. entonces debe imprimirlo ya que la división de esos números por 3 da como resto 0, exacto.

3 / 3 = 1, resto 0
6 / 3 = 2, resto 0
Distinto de:

4 / 3 = 1, resto 1
Hint de ayuda: en programación, hay un símbolo que ocupamos para saber inmediatamente el resto, en lugar de hacer la división y luego ver el resto. En python es el símbolo %, por ejemplo:"""

#comentario: for: permite realizar operaciones repetitivas de manera sencilla y eficiente.

for x in range(100):
  if (x+1) % 3 == 0:
    print(x+1)

"""3.**Pseudocódigo, Sumador y comparador de dos números:**

 Realiza el algoritmo para un sumador de dos números. Si el resultado es menor a 100 se mostrará el mensaje "menor a 100", si el resultado es mayor a 100, pero menor a 150 mostrará el mensaje "mayor a 100", pero si es mayor a 150 mostrará el mensaje "mayor a 150".
"""

#comentario: if: permite ejecutar el código Python si se cumple una condición. elif: se usa para comprobar múltiples condiciones si una condición es falsa

numero_1 = int(input("Ingresa un número"))
numero_2 = 5
suma = numero_1 + numero_2
resultado = ""

if(suma<100):
  resultado = "menor a 100"
elif(suma>=100 and suma<150):
  resultado = "mayor a 100"
elif(suma>=150):
  resultado = "mayor a 150"

print(resultado)

"""**Problema 4. Pseudocódigo, Calculador de promedio**
Generar un programa que combine variables, tipos de datos y una condicional en Python (hacer una función que evalúe si el usuario es mayor de edad y si le gusta la programación, que envíe diferentes textos según la respuesta del usuario)
"""

#comentario: def: indica a Python que una nueva función está siendo definida. lower: baja todo a minúscula

def calculador_de_promedio():
 nombre = input("ingresa nombre: ")
 edad = int(input("¿cuántos años tienes? "))
 gusta_programar = (input("¿te gusta proigramar? (si/no)")). lower()
 if edad >= 18 and gusta_programar == "si":
  print (f"{nombre}, eres mayor de edad y te gusta la programación. bacán")
 elif edad >= 18:
  print (f"{nombre}, eres mayor de edad y no te gusta la programación. bueno ")
 else:
    print(f"{nombre}, eres menor de edad. intentalo ")

calculador_de_promedio ()