#Cree una función que tome un número como entrada e imprima
def EntradaNumero(Entrada):
    if Entrada == "":
        print("Ingrese un dato ")
        return None
    else:
        print(f"Numero ingresado es: {Entrada}")
        return Entrada

Num = input("Ingrese un numero: ")
resultado = EntradaNumero(Num)

# Verificar si el resultado es None antes de imprimir
if resultado is not None:
    print(resultado)
else:
    print("No se ingresó un número válido.")
