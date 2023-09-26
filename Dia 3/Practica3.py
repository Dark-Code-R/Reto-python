#numero primo 
Num=int(input("Inserte un numero para saber si es para o no : "))
if Num>1:
    cont=0
    for i in range (2, Num):
        resto=Num%i
        if resto ==0:
            cont=+1

    if cont ==0:
        print("el {} es un numero primo".format(Num))
    else:
        print("el {} es un numero no primo".format(Num))