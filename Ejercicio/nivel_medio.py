#Define una función que utilice un bucle para imprimir los primeros n numeros de la serie de Fibonacci
def imprimir_fibonacci(n):
    fibonacci = [0, 1]
    for _ in range(2, n):
        siguiente_numero = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(siguiente_numero)
    for numero in fibonacci[:n]:
        print(numero, end=" ")
n = 10
print(imprimir_fibonacci(n))

#Define una función que tome un número y retorne una lista de sus divisores
def obtener_divisores(numero):
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores
numero_ingresado = 12
lista_divisores = obtener_divisores(numero_ingresado)
print(f"Los divisores de {numero_ingresado} son {lista_divisores}")

#Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.

def obtener_elementos_unicos(lista):
    return list(set(lista))
lista_original = [1, 2, 3, 2, 4, 5, 3, 6]
lista_unicos = obtener_elementos_unicos(lista_original)
print(f"Lista original: {lista_original}")
print(f"Lista con elementos unicos: {lista_unicos}")

#Define una función que tome un número y retorne la suma de sus dígitos
def suma_digitos(numero):
    suma = 0
    numero_absoluto = abs(numero)
    while numero_absoluto > 0:
        digito = numero_absoluto % 10
        suma += digito
        numero_absoluto //= 10
    return suma
numero_ingresado = 12345
resultado_suma_digitos = suma_digitos(numero_ingresado)
print(f"La suma de los digitos de {numero_ingresado} es: {resultado_suma_digitos}")

#Define una función que tome una cadena y cuente el número de vocales de la cadena.

def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    cantidad_vocales = sum(1 for char in cadena if char in vocales)
    return cantidad_vocales
cadena_ingresadas = "Hola, Mundo"
resultado_contador = contar_vocales(cadena_ingresadas)
print(f"LA cantidad de vocales en {cadena_ingresadas} es {resultado_contador}")

#Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista

def primeros_n_elementos(lista, n):
    return lista[:n]
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n_elementos_deseados = 4
resultado = primeros_n_elementos(mi_lista, n_elementos_deseados)
print(f"Los primeros {n_elementos_deseados} elementos de la lista son {resultado}")

#Define una función que tome una cadena y retorne la cantidad de letras mayusculas y minusculas en la cadena

def contar_mayusculas_minusculas(cadena):
    contador_mayusculas = sum(1 for char in cadena if char.isupper())
    contador_minusculas = sum(1 for char in cadena if char.islower())
    return contador_mayusculas, contador_minusculas
cadena_ingresada = "Hola Mundo!"
mayusculas, minusculas = contar_mayusculas_minusculas(cadena_ingresada)
print(f"Cantidad de mayusculas: {mayusculas}")
print(f"Cantidad de minusculas: {minusculas}")

#Define una función que tome un número y retorne True si es un
#número perfecto, False en caso contrario. Un número perfecto es aquel que es
#igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número
#perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.

def es_numero_perfecto(numero):
    if numero <= 0:
        return False
    suma_divisores = sum(i for i in range(1, numero) if numero % i == 0)
    return suma_divisores == numero
numero_ingresado = 28
resultado = es_numero_perfecto(numero_ingresado)
if resultado:
    print(f"{numero_ingresado} es un numero perfecto.")
else:
    print(f"{numero_ingresado} no es un número perfecto.")

#Define una función que reciba un número y retorne su representación en binario.

def representacion_binaria(numero):
    if numero < 0:
        return "No se admiten numeros negativos para representación binaria"
    else:
        return bin(numero)[2:]
numero_ingresado = 42
resultado_binario = representacion_binaria(numero_ingresado)
print(f"la representacion binaria de {numero_ingresado} es: {resultado_binario}")

#Define una funcion que reciba dos listas y retorne la intersección de ambas (Los elementos que están en las dos listas)

def interseccion_listas(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    interseccion = list(conjunto1 & conjunto2)
    return interseccion
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
resultado_interseccion = interseccion_listas(lista1, lista2)
print(f"Interseccion de las listas: {resultado_interseccion}")

#Define una función que tome una cadena y determine si es un palíndromo (Se lee igual de izquierda a derecha que de derecha a izquierda)

def es_palindromo(cadena):
    cadena_sin_espacios = ''. join(c for c in cadena if c.isalnum())
    cadena_invertida = cadena_sin_espacios[::-1]
    return cadena_sin_espacios.lower() == cadena_invertida.lower()
cadena_ingresada = "Anita lava la tina"
if es_palindromo(cadena_ingresada):
    print(f"'{cadena_ingresada} es un palíndromo.")
else:
    print(f"{cadena_ingresada} no es un palíndromo.")

#Escribe un programa que imprima los numeros del 1 al 50, pero para múltiplos de tres imprima "Fizz" en lugar del número y para 
#los multiplos de 5 imprima "Buzz". Para números que son multiplos de tanto de tres como cinco imrpima "FizzBuzz"

def fizzbuzz():
    for numero in range(1, 51):
        if numero % 3 == 0 and numero % 5 == 0:
            print("FizzBuzz")
        elif numero % 3 == 0:
            print("Fizz")
        elif numero % 5 == 0:
            print("Buzz")
        else:
            print(numero)
print(fizzbuzz())

#Defina una función que tome una lista y retorne la lista ordenada en orden ascendente
def ordenar_ascendente(lista):
    return sorted(lista)
mi_lista = [4, 2, 8, 1, 5]
lista_ordenada = ordenar_ascendente(mi_lista)
print(f"Lista original: {mi_lista}")
print(f"Lista ordenada en orden ascendente: {lista_ordenada}")

#Define una función que reciba una lista de palabras y un entere n, y retorne la lista de palabras que son más largas que n.

def palabras_mas_largas_que_n(lista_palabras, n):
    return [palabra for palabra in lista_palabras if len(palabra) > n]

lista_palabras = ["gato", "perro", "elefante", "tigre", "leon"]
n = 5
resultado = palabras_mas_largas_que_n(lista_palabras, n)
print(f"Palabras mas largas que {n}: {resultado}")

#Define una función que tome un número y calcule su serie de Fibonacci

def fibonacci(n):
    if n <= 0:
        return "Ingrese un numero entero positivo mayor que cero"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        resultado = [0, 1]
        while len(resultado) < n:
            resultado.append(resultado[-1] + resultado[-2])
        return resultado 
n = 10
resultado_fibonacci = fibonacci(n)
print(f"Serie de Fibonacci hasta el {n} -ésimo termino: {resultado_fibonacci}")

#Define una función que tome una lista de números y retorne el número mas grande de la la lista.

def encontrar_maximo(lista):
    if not lista:
        return "La lista esta vacía, no hay máximo."
    else:
        maximo = max(lista)
        return maximo 
lista_numeros = [15, 7, 22, 45, 9, 33]
resultado_maximo = encontrar_maximo(lista_numeros)
print(f"El número mas grande de la lista es: {resultado_maximo}")

#Defina una función que reciba un número y retorne la suma de sus dígitos al cubo.

def suma_cubos_digitos(numero):
    suma_cubos = sum(int(digito) ** 3 for digito in str(abs(numero)))
    return suma_cubos
numero_ingresado = 123
resultado_suma_cubos = suma_cubos_digitos(numero_ingresado)
print(f"La suma de los cubos de los digitos de {numero_ingresado} es: {resultado_suma_cubos}")

#Define una función que reciba una lista de números y retorne el segundo número mas grande de la lista.

def segundo_mas_grande(lista):
    if len(lista) < 2:
        return "La lista debe tener al menos dos números"
    lista_ordenada = sorted(lista, reverse=True)
    segundo_mas_grande = lista_ordenada[1]
    return segundo_mas_grande
numeros = [4, 10, 7, 2, 8]
resultado = segundo_mas_grande(numeros)
print(f"El seundo número mas grande es: {resultado}")

#Define una función que tome dos listas y retorne True si tiene al menos un miembro en común, de los contrario, retorne False

def tienen_miembro_comun(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True
    return False
lista_a = [1, 2, 3, 4, 5]
lista_b = [6, 7, 8, 9, 10]
resultado = tienen_miembro_comun(lista_a, lista_b)
print(resultado)

#Define una función que tome una lista y retoirne una nueva lista con los elementos de la liosta original en orden inverso

def lista_inversa(original):
    lista_inversa = original.copy()
    lista_inversa.reverse()
    return lista_inversa
mi_lista = [1, 2, 3, 4, 5]
resultado = lista_inversa(mi_lista)
print(f"El resultado inverso de la lista: {mi_lista} es {resultado}")

#Defina una función que reciba una cadena y cuente el número de dígitos y letras que contiene

def contar_digitos_y_letras(cadena):
    num_digitos = 0
    num_letras = 0
    for caracter in cadena:
        if caracter.isdigit():
            num_digitos += 1
        elif caracter.isalpha():
            num_letras += 1
    return num_digitos, num_letras
entrada = "Hola123Mundo456"
digitos, letras = contar_digitos_y_letras(entrada)
print(f"Número de digitos: {digitos}")
print(f"Número de letras: {letras}")

#Define una función que reciba una lista de números y retorne la suma acumulada de los números 

def suma_acumulada(lista):
    suma_acumulada = 0
    resultados_parciales = []
    for numero in lista:
        suma_acumulada += numero
        resultados_parciales.append(suma_acumulada)
    return resultados_parciales
numeros = [1, 2, 3, 4, 5]
resultado = suma_acumulada(numeros)
print(f"La suma acumulado de {numeros} es {resultado}")

#Defina una función que encuentre el elemento mas común en una lista

def elemento_mas_comun(lista):
    if not lista:
        return None
    elemento_mas_comun = max(set(lista), key=lista.count)
    return elemento_mas_comun
mi_lista = [1, 2, 3, 2, 4, 5,4, 4, 4,7]
resultado = elemento_mas_comun(mi_lista)
print(f"El elemento mas común es: {resultado}")

#Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10
def tabla_de_multiplicar(numero):
    if not isinstance(numero, (int, float)):
        return "Ingresa un número válido"
    tabla = {}
    for i in range(1, 11):
        tabla[i] = numero * i
    return tabla
mi_numero = 7
resultado = tabla_de_multiplicar(mi_numero)
print(f"Tabla de multiplicar de {mi_numero}: \n{resultado}")

#Define una función que tome una cedna y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena

def contar_apariciones(cadena):
    apariciones = {}
    for caracter in cadena:
        apariciones[caracter] = apariciones.get(caracter, 0) + 1
    return apariciones
mi_cadena = "Python es genial"
resultado = contar_apariciones(mi_cadena)
print(resultado)

#Define una función que tome dos listas y retorne la lista de elementos que no estan en ambas listas

def elementos_no_comunes(lista1, lista2):
    no_comunes = set(lista1) ^ set(lista2)
    return list(no_comunes)
lista_a = [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]
resultado = elementos_no_comunes(lista_a, lista_b)
print(resultado)

#Define una función que tome una lista y retorne la lista sin duplicados.

def eliminar_duplicados(lista):
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados
mi_lista = [1, 2, 2, 3, 4, 4, 5]
resultado = eliminar_duplicados(mi_lista)
print(resultado)

#Define una función que reciba un número entero positico y retorne la suma de los cuadrados de todos los números para menores o iguales a ese número.

def suma_cuadrados_pares(n):
    if not isinstance(n, int) or n < 1:
        return "Por favor, ingresa un número entero positivo"
    suma = sum(x**2 for x in range(1, n+1) if x % 2 == 0)
    return suma
numero = 6
resultado = suma_cuadrados_pares(numero)
print(f"La suma de los cuadrados de los números pares hasta {numero} es: {resultado}")

#Define una función que reciba una lista de números y retorne el promedio de los números en la lista.

def promedio_lista(lista):
    if not lista:
        return "La lista esta vacía, no se puede calcular el promedio"
    promedio = sum(lista) / len(lista)
    return promedio 
numeros = [2, 4, 6, 8, 10]
resultado = promedio_lista(numeros)
print(f"El promedio de la lista es: {resultado}")

#Define una función que reciba una lista de cadenas y retorne la cadenas mas larga en la lista.
def cadena_mas_larga(lista):
    if not lista:
        return "La lista esta vacía, no hay cadena mas larga"
    cadena_mas_larga = max(lista, key=len)
    return cadena_mas_larga
cadenas = ["python", "java", "javascript", "c++", "ruby"]
resultado = cadena_mas_larga(cadenas)
print(f"La cadena mas larga es: {resultado}")

#Defina una función que reciba un número entero n y retorne una lista con los n primeros números primos

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def n_primeros_primos(n):
    if not isinstance(n, int) or n <= 0:
        return "Por favor, ingresa un número entero positivo mayor que cero"
    numeros_primos = []
    candidato = 2
    while len(numeros_primos) < n:
        if es_primo(candidato):
            numeros_primos.append(candidato)
        candidato += 1
    return numeros_primos
n = 5
resultado = n_primeros_primos(n)
print(f"Los primeros {n} numeros primos son: {resultado}")

#Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.

def invertir_palabras(cadena):
    palabras = cadena.split()
    palabras_invertidas = palabras[::-1]
    resultado = ' '.join(palabras_invertidas)
    return resultado
cadena_original = "Hola mundo, estoy aprendiendo Python"
resultado_invertido = invertir_palabras(cadena_original)
print(f"Cadena original:", cadena_original)
print(f"Cadena invertida:", resultado_invertido)

#Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.

def ordenar_por_ultimo_elemento(lista_de_tuplas):
    lista_ordenada = sorted(lista_de_tuplas, key=lambda x: x[-1])
    return lista_ordenada
tuplas_a_ordenar = [(1, 3, 5), (4, 2, 8), (7, 1, 6), (2, 9, 0)]
resultado_ordenado = ordenar_por_ultimo_elemento(tuplas_a_ordenar)
print("Lista original de tuplas:", tuplas_a_ordenar)
print("Lista ordenada por ultimo elemento:", resultado_ordenado)

#Define uan función que reciba una cadena y retorne lña cantidad de letras vocales en la cadena

def contar_vocales(cadena):
    cadena = cadena.lower()
    vocales = "aeiou"
    cantidad_vocales = sum(1 for letra in cadena if letra in vocales)
    return cantidad_vocales
cadena_ejemplo = "Hola, estoy contando las vocales en esta cadena"
cantidad_vocales_resultado = contar_vocales(cadena_ejemplo)
print("Cadena", cadena_ejemplo)
print("Cantidad de vocales:", cantidad_vocales_resultado)


#Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero_ejemplo = 17
resultado_primo = es_primo(numero_ejemplo)
print(f"¿{numero_ejemplo} es primo? {resultado_primo}")


    


