#Implementar una función que devuelva el factorial de un número determinado mediante recursividad
def factorial(n):
    # Caso base: factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)
numero =int(input("Ingrese un numero: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")
