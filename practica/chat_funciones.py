def responder(mensaje):
    return "Dijiste: " + mensaje

def guardar(historial,role,content,hora):
    historial.append({"role": role, "content": content, "hora": hora})