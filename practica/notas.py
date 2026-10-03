notas = []

while True:
    nota = input("¿Qué nota quieres agregar? ")
    
    if nota.lower() == "fin":
        break
    try:
        nota = float(nota)
    except ValueError:
        print("Por favor, ingresa una nota válida.")
        continue
    if nota < 0 or nota > 5:
        print("Por favor, ingresa una nota válida.")
        continue
    notas.append(nota)

if len(notas) == 0:
    print("No hay notas para calcular.")
    exit()
 
print("--------------------------------")
print(f"Has ingresado {len(notas)} notas")
promedio = sum(notas) / len(notas)
mas_alta = max(notas)
mas_baja = min(notas)
if promedio >= 3:
    estado = "aprobado"
else:
    estado = "reprobado"

print(f"Las notas son: {notas}")
print(f"La nota promedio es: {promedio}")
print(f"La nota más alta es: {mas_alta}")
print(f"La nota más baja es: {mas_baja}")
print(f"El estado es: {estado}")

