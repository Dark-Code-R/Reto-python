# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número para calcular su factorial: "))
factorial = 1
# Verificar si el número es negativo
if numero < 0:
    print("El factorial no está definido para números negativos.")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    # Calcular el factorial
    for i in range(1, numero + 1):
        factorial *= i

    print(f"El factorial de {numero} es {factorial}")
