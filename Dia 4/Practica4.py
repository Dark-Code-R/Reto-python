#Crea una función para encontrar el cuadrado de cada elemento en una lista determinada.
def Lista_De_Datos(lista):
    resultado = []
    for x in lista:
        resultado.append(x**2)
    return resultado

Num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = Lista_De_Datos(Num)
print(f"Lista original: {Num}")
print(f"Cuadrado de cada elemento: {res}")
