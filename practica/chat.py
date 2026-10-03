import datetime

historial = []


while True:
    mensaje = input("¿Qué quieres decir? ")
    hora = datetime.datetime.now().strftime("%H:%M")
    if mensaje.lower() == "salir":
        break
    historial.append({"role": "user", "content": mensaje, "hora": hora})
    historial.append({"role": "assistant", "content": "Dijiste: " + mensaje, "hora": hora})
    

for mensaje in historial:
    print(f"{mensaje['hora']} - {mensaje['role']}: {mensaje['content']}")