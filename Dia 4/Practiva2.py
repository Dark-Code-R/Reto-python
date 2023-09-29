#Funcion para saber si es palindromo o no
Cadena=str(input("Ingrese la palabra para identificarlo: "))
res= Cadena[::-1]
if Cadena == res :
    print("La palabra es palindromo ")
else:
    print("La palabra no es palindromo")