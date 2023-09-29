#Implementar una función para comprobar si un año determinado es bisiesto o no.
def Añobisiesto(Año):
    Año=int(Año)
    if Año % 400 == 0:
        print("Es año bisiesto ")
    else:
        print("No es año bisiesto")
Num=input("Ingrese el año: ")
Añobisiesto(Num) 
