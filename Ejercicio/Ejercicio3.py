'''Bucles
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while . 
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    print(numero)

i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1
    
x = 1
suma = 0
while x <= 100:
    suma = suma + x
    x += 1
print("La suma de los número del 1 al 100 es:",suma)
