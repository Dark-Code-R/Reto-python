#Escriba una función para verificar si un número es par o impar y devuelva "Par" o "Impar" en consecuencia
def Par_o_impar (Numero):
    if Numero % 2 == 0:
        print("Es par")
    else :
        print("Es impar")

Num=int(input("Inserte el número: "))
Par_o_impar(Num)