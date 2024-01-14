'''Condicionales
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.'''

x = 6
if x > 0:
    print("Este número es positivo")
else:
    print("Este número es negativo")

a = 6
if a % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

b = 4
c = 6
d = 1
if b > c and b > d:
    print("El número mnayor es:", b)
elif c > b and c > d:
    print("El número mayor es:", c)
elif d > b and d > c:
    print("El numero mayor es:", d)
else:
    print("no hay número mayor")
    