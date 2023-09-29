#Escriba una función que tome dos listas y devuelva su intersección (elementos comunes) 
def ElementosComunes(Datos1, Datos2):
    interseccion = set(Datos1) & set(Datos2)
    if interseccion:
        return sorted(list(interseccion))
    else:
        return "No hay datos iguales"

Datos1 = ["Juan", "Rober",  "Lucas", "Antoni"]
Datos2 = ["Juan", "Maria", "Antoni"]
Res = ElementosComunes(Datos1, Datos2)
print(f"La primera lista tiene estos datos: {Datos1}")
print(f"La Segunda lista tiene estos datos: {Datos2}")
print(f"El dato que se repeti en las 2 listas es: {Res}")
