#Guardar datos enteros en una lista
lista1=[1,2,3,4,5,12,51,23,51,35,13,23,43,65,76]
print ("Estos son los datos de la lista: ",lista1)
newlist=[]
for x in lista1:
    if x % 2 ==0:
        newlist.append(x)
        print(newlist)
