# bucle entre numero primos 1 y 50
def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Imprimir todos los números primos entre 1 y 50
print("Números primos entre 1 y 50:")
for num in range(1, 51):
    if es_primo(num):
        print(num)
