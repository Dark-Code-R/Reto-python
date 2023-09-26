#tabla de multipplicar por un numero dado
num = int(input("Ingresa un número: "))

print(f"Tabla de multiplicar del {num}:")
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
