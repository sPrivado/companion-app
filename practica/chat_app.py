import datetime
from chat_funciones import responder, guardar

historial = []


while True:
    mensaje = input("¿Qué quieres decir? ")
    hora = datetime.datetime.now().strftime("%H:%M")
    if mensaje.lower() == "salir":
        break   
    guardar(historial, "user", mensaje, hora)
    respuesta = responder(mensaje)
    print(respuesta)
    guardar(historial, "assistant", respuesta, hora)
    

for mensaje in historial:
    print(f"{mensaje['hora']} - {mensaje['role']}: {mensaje['content']}")