# Importamos las bibliotecas necesarias
import requests
import schedule
import time
from data import numeros
# Definimos la función para enviar mensajes
def sendMessage(para, mensaje):
    # URL del servidor al que se enviará la solicitud POST
    url = 'http://localhost:3001/lead'
    
    # Datos que se enviarán en la solicitud POST
    data = {
        "message": mensaje,
        "phone": para
    }
    
    # Encabezados HTTP para la solicitud
    headers = {
        'Content-Type':'application/json'
    }
    
    # Imprimimos los datos que se enviarán
    print(data)
    
    # Hacemos la solicitud POST y devolvemos la respuesta del servidor
    response = requests.post(url, json=data, headers=headers)
    return response

phone_numbers = ['584246302064']
# Mensajes que se enviarán
messages = ['Hola esto es un bot, espero estes bien esta es una prueba de envio de mensajes' 
            'masivos luego de este mensaje te llegaran cuatro mensajes a distintas horas mencionandote'
            'la hora a la que se debria haber enviado el mensaje de ser asi responde con un pulgar hacia arriba \U0001F44D.\nSon las 11:00am', 
            'Hola son las 11:05am.\nSolo quedan 3 mensajes',
            'Hola son las 11:15am.\nSolo quedan 2 mensajes',
            'Hola son las 11:30am.\nSolo queda un mensaje', 
            'Hola son las 12:00m\nA comeeeeer \U0001F3C3\nYa no quedan mas mensajes\U0001F625',
            'JAJA si faltaba uno\nGracias por soportarme \U0001F917']

# Horarios en los que se enviarán los mensajes
schedule_times = ['12:07','11:05','11:15','11:30','12:00','12:00']

# Programamos las tareas para enviar los mensajes
for sch_time, msg in zip(schedule_times, messages):
    for phone in phone_numbers:
        # Para cada combinación de horario y mensaje, programamos una tarea para enviar ese mensaje a cada número de teléfono
        schedule.every().day.at(sch_time).do(sendMessage, phone, msg)

# Ejecutamos un bucle infinito que ejecuta todas las tareas programadas que deberían ejecutarse en ese momento
while True:
    schedule.run_pending()
    time.sleep(1)
