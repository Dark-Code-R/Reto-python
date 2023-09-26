# Calcula la suma de dígitos de un número dado
numero = int(input("Ingresa un número: "))
suma_digitos = 0

while numero > 0:
    # Obtener el último dígito
    digito = numero % 10
    # Sumar el dígito al total
    suma_digitos += digito
    # Eliminar el último dígito
    numero //= 10
print(f"La suma de los dígitos es: {suma_digitos}")
