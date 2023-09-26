# contador de 5 palabras
palabras = ["manzana", "banana", "uva", "sandía", "pera", "naranja", "kiwi"]
contador = 0

for palabra in palabras:
    # Verificar si la longitud de la palabra es mayor que cinco
    if len(palabra) > 5:
        contador += 1
print(f"Número de palabras con más de cinco caracteres: {contador}")
