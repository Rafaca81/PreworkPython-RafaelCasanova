#Crea una función para verificar si un número es par o impar y devuelva “El
#número es par” o “El número es impar” según corresponda.
def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "El numero es par."
    else:
        return "El número es impar."
numero_ingresado = 4
resultado_verificacion = verificar_par_impar(numero_ingresado)
print(resultado_verificacion)

#Crea una función a la que pases un número como argumento, calcule el factorial
#de ese número y haga print del resultado.
def calcular_factorial(numero):
    factorial_resultado = 1
    for i in range(1, numero + 1):
        factorial_resultado *= i
    print(f"El factorial de {numero} es: {factorial_resultado}")
numero_ingresado = 7
print(calcular_factorial(numero_ingresado))

#Crea una función a la que se le pase un número como argumento, calcule la
#cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado
#total de dígitos.

def contar_digitos(numero):
    numero_str = str(numero)
    cantidad_digitos = len(numero_str)
    print(f"La cantidad de digitos en {numero} es: {cantidad_digitos}")

numero_ingresado = 12345
print(contar_digitos(numero_ingresado))

#Dada una lista de números, crea una función que devuelva el número máximo de la lista

def encontrar_maximo(lista):
    if not lista:
        return None 
    else:
        maximo = max(lista)
        return maximo
lista_numeros = [12, 45, 23, 67, 9, 104]
resultado_maximo = encontrar_maximo(lista_numeros)
if resultado_maximo is not None:
    print(f"El numero maximo de la lista es: {resultado_maximo}")
else:
    print("La lista está vacía.")

#Crea una función que, dado un número, sume los digitos de ese número y devuelva el resultado
    
def sumar_digitos(numero):
    suma = 0
    numero_absoluto = abs(numero)
    while numero_absoluto > 0:
        digito = numero_absoluto % 10
        suma += digito
        numero_absoluto //= 10
    return suma
numero_ingresado = 456
resultado_suma_digitos = sumar_digitos(numero_ingresado)
print(f"La suma de los digitos de {numero_ingresado} es: {resultado_suma_digitos}")
#La funcion usa el bucle "while" para iterar los digitos del numero. En cada iteración, se obtiene el último digito usando el operador "%"
#Y se agrega a la suma. Luego elimina el ultimo digito diviendo el número por 10. Este proceso lo repetimos hasta llegar a cero

#Dados dos números, crea una función para encontrar el mínimo común múltiplo
#(MCM) de los dos números, que se les pasarán como argumento a la función, y
#devuelva el MCM
def calcular_mcm(num1, num2):
    def calcular_mcd(a, b):
        while b:
            a, b = b, a % b
        return a
    if num1 == 0 or num2 == 0:
        return 0
    else:
        mcd = calcular_mcd(num1, num2)
        mcm = (num1 * num2) // mcd
        return mcm
numero1 = 6
numero2 = 8
resultado_mcm = calcular_mcm(numero1, numero2)
print(f"El mínimo Común Múltiplo de {numero1} y {numero2} es: {resultado_mcm}")

#Crea una función a la que, pasándole la base y la altura, calcule y devuelva el
#área de un triángulo
def calcular_area_triangulo(base, altura):
    area = 0.5 * base * altura
    return area
base_triangulo = 10
altura_triangulo = 8
resultado_area = calcular_area_triangulo(base_triangulo, altura_triangulo)
print(f"El area del triangulo con base {base_triangulo} y altura {altura_triangulo} es {resultado_area}")

  #Crea una función que, dado un número, verifique si un número es positivo, negativo o cero
def verificar_positivo_negativo_cero(numero):
    if numero > 0:
        return "El número es positivo."
    elif numero < 0:
        return "El número es negativo."
    else:
        return "El número es cero."

numero_ingresado = -4
resultado_verificacion = verificar_positivo_negativo_cero(numero_ingresado)  
print(resultado_verificacion)

# Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.
def contar_letras(palabra):
    cantidad_letras = sum(c.isalpha() for c in palabra)
    return cantidad_letras
palabra_ingresada = "HolaMundo123"
resultado_contador = contar_letras(palabra_ingresada)
print(f"La cantidad de letras en {palabra_ingresada} es {resultado_contador}")

#Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto.

def valor_absoluto_lista(lista):
    lista_absoluta = [abs(numero) for numero in lista]
    return lista_absoluta
lista_numeros = [-5, 10, -3, 7, -1]
lista_absoluta_resultado = valor_absoluto_lista(lista_numeros)
print(f"La lista original: {lista_numeros}")
print(f"La lista con valores absolutos: {lista_absoluta_resultado}")

#Crea una función que, dado un numero, verifique si es un número es primo.

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero_ingresado = 17
if es_primo(numero_ingresado):
    print(f"{numero_ingresado} es un número primo.")
else:
    print(f"{numero_ingresado} no es un número primo.")

#Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números.

def calcular_mcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
numero1 = 36
numero2 = 48
resultado_mcd = calcular_mcd(numero1, numero2)
print(f"EL Máximo Común Divisor de {numero1} y {numero2} es: {resultado_mcd}")
