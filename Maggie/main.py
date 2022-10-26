# Importamos la librería para poder hacer una llamada
import requests,time
from requests.models import Response
import pandas as pd
import os.path

lista_general = list()
lista_homer = list()
lista_lisa = list()

def obtener_quote():
  URL ='https://thesimpsonsquoteapi.glitch.me/quotes'
  respuesta :Response = requests.get(url = URL)
  # Extraemos los datos en formato JSON
  datos = respuesta.json()
  # Obtenemos valor de la frase y el nombre en la claves del JSON que nos interesa
  s_quote = datos[0]
  quote = s_quote['quote']
  name = s_quote['character']
  # Guardamos en un csv "General" las frases que no sean de Homer ni Lisa

  if name != "Homer Simpson" and name != "Lisa Simpson":
    
    # Verificamos si está creado el csv general
    file_general = os.path.isfile("app/General/General.csv")
    
    if file_general == True:
      
      lista_general.append ([name,quote])
      df = pd.DataFrame(lista_general)
      df.to_csv('app/General/General.csv', mode='a', index=False, header=False)
    
    else:

      header_name = ['Nombre', 'Frase']
      lista_general.append ([name,quote])
      df = pd.DataFrame(lista_general)
      df.to_csv('app/General/General.csv', index=False, header=header_name)

  # Guardamos en un csv "Homer" solo las frases de Homer

  elif name == "Homer Simpson":
    
    # Verificamos si está creado el csv homer
    file_homer = os.path.isfile("app/Homer/Homer.csv")

    if file_homer == True:
      
      lista_homer.append ([name,quote])
      df = pd.DataFrame(lista_homer)
      df.to_csv('app/Homer/Homer.csv', mode='a', index=False, header=False)
    
    else:

      header_name = ['Nombre', 'Frase']
      lista_homer.append ([name,quote])
      df = pd.DataFrame(lista_homer)
      df.to_csv('app/Homer/Homer.csv', index=False, header=header_name)
      
  # Guardamos en un csv "Lisa" solo las frases de Lisa

  elif name == "Lisa Simpson":
    
    # Verificamos si está creado el csv lisa
    file_lisa = os.path.isfile("app/Lisa/Lisa.csv")

    if file_lisa == True:
      
      lista_lisa.append ([name,quote])
      df = pd.DataFrame(lista_lisa)
      df.to_csv('app/Lisa/Lisa.csv', mode='a', index=False, header=False)
    
    else:
      header_name = ['Nombre', 'Frase']
      lista_lisa.append ([name,quote])
      df = pd.DataFrame(lista_lisa)
      df.to_csv('app/Lisa/Lisa.csv', header=header_name)

  return print(name + ": " + quote)

 # Generamos una frase cada 30s y la guardamos

def esperar():
  while True:
    obtener_quote()
    print
    time.sleep(30)


print (esperar())