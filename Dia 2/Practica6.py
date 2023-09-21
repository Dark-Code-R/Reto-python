print("DIAS-MES-AÑO")
dias = int(input("Ingresa el número de días: "))
anos = dias // 365
semanas = (dias % 365) // 7
dias_restantes = (dias % 365) % 7

print(f"{dias} dias equivalen a {anos} años, {semanas} semanas y {dias_restantes} días.")
