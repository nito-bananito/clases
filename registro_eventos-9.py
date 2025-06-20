# Programa: Registro de eventos en un archivo log

from datetime import datetime

def registrar_evento(nombre_archivo_log, mensaje_evento):
    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea_log = f"[{fecha_hora_actual}] {mensaje_evento}\n"

    try:
        with open(nombre_archivo_log, 'a', encoding='utf-8') as archivo_log:
            archivo_log.write(linea_log)
        print("Evento registrado con éxito.")
    except Exception as e:
        print(f"Ocurrió un error al registrar el evento: {e}")

# Solicitar mensaje al usuario
mensaje = input("Ingresa el mensaje del evento: ")
registrar_evento("log.txt", mensaje)
