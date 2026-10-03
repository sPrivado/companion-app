nombre = input("¿Cuál es tu nombre? ")

while True:
    try:
        edad = int(input("¿Cuál es tu edad? "))
        
    except ValueError:
        print("Por favor, ingresa una edad válida.")
        continue

    if edad < 0 or edad > 100:
        print("Por favor, ingresa una edad válida.")
        continue
    break

if edad >= 18:
    estado = "mayor de edad."
else:
    estado = "menor de edad."

print(f"Hola, {nombre}! Tienes {edad} años y eres {estado}")