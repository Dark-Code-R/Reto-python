#Secuencia Fibonicci
m=int(input("ingrese hasta que numero quiere la secuencia :"))
u = 0 
v= 1
if m< 0:
    print (" dato incorrecto ")
elif m==0:
    print(u) 
elif m ==1 :
    print(v)
else:
    for i in  range (2,m):
        c=u+v
        u= v
        v=c
        print(v)