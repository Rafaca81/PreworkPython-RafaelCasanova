'''Funciones
1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa.'''

def suma_numeros(a, b):
    suma = a + b
    return suma
resultado = suma_numeros(8, 4)
print(resultado)


def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
numero_ingresado = 5
resultado_factorial = factorial(numero_ingresado)
print(f"El factorial de {numero_ingresado} es: {resultado_factorial}")

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2 , int (numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero_ingresado = 13
if es_primo(numero_ingresado):
    print(f"{numero_ingresado} es un numero primo.")
else:
    print(f"{numero_ingresado} no es un numero primo.")
#La función "es_primo" toma un número como argumento y realiza un bucle desde 2 hasta la raíz cuadrada del número. Si el número es divisible
#por algun otro número dentro de este rango, entonces no es primo. En caso contratio si se considera primo.
    

def suma_lista(numeros):
    suma = sum(numeros)
    return suma
lista_numeros = [1, 2, 3, 4, 5]
resultado_suma = suma_lista(lista_numeros)
print(f"La suma de la lista {lista_numeros} es : {resultado_suma}")

def reversa_cadena(cadena):
    cadena_reversa = cadena[::-1]
    return cadena_reversa

texto_ingresado = "Hola, mundo!"
resultado_reversa = reversa_cadena(texto_ingresado)
print(f"La cadena reversa de '{texto_ingresado}' es: '{resultado_reversa}")



    