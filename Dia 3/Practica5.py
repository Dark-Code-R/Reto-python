#seleccionar nombres que empiezen con A
Nombres=["Rodrigo","Naira","Andres","Alisson","Roberto","Juan","Ademar","Antonio","Amaranto"]
for nombre in Nombres:
    #stratswitch es para buscar la primera letra que empeze con el dato que le des
    if nombre.startswith('A'):
      print(nombre)
