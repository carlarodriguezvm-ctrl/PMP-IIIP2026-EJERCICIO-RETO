from datetime import datetime

edad_jubilacion = 60

def calcular_edad(fecha_nacimiento):
    hoy = datetime.now().date()
    cumplio_anios = (hoy.month, hoy.day) >= (fecha_nacimiento.month, fecha_nacimiento.day)
    edad = hoy.year - fecha_nacimiento.year
    
    if not cumplio_anios:
        edad -= 1
        
    return edad, hoy


def procesar_jubilacion(fecha_txt):
    try:
        fecha_nacimiento = datetime.strptime(fecha_txt, "%d/%m/%Y").date()
        edad, hoy = calcular_edad(fecha_nacimiento)

        if fecha_nacimiento > hoy:
            mensaje = "La fecha de nacimiento no puede ser mayor a la fecha actual."
            return mensaje
        
        if edad >= edad_jubilacion:
            mensaje = f"Tienes {edad} años. Ya puedes pensar en jubilarte."
            return mensaje
        else:
            anios_faltan = edad_jubilacion - edad
            mensaje = f"Tienes {edad} años. Te faltan {anios_faltan} años para jubilarte."
            return mensaje

    except ValueError:
        mensaje = "Formato de fecha inválido. Por favor, ingresa la fecha en formato dd/mm/aaaa."
        return mensaje


print(calcular_edad(datetime(2006, 5, 11).date()))  # Muestra (20, date(2026, 10, 3))
print(calcular_edad(datetime(2006, 12, 8).date()))  # Muestra (19, date(2026, 10, 3))

print(procesar_jubilacion("11/05/2006"))  # Tienes 20 años. Te faltan 40 años para jubilarte.
print(procesar_jubilacion("08/12/2006"))  # Tienes 19 años. Te faltan 41 años para jubilarte.