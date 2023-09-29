#Calcula el área de un triángulo dada su base y altura usando una función.
def DatosTriangulo(base, altura):
    if base <= 0 or altura <= 0:
        print("Ingrese valores válidos para la base y la altura.")
        return None
    else:
        return (base * altura) / 2

base = float(input("Ingrese el dato de base: "))
altura = float(input("Ingrese el dato de altura: "))

area = DatosTriangulo(base, altura)

if area is not None:
    print("El área del triángulo es:", area)

