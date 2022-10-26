# Importamos la librería para poder hacer una llamada

from email.mime import image
import string
from unicodedata import name
import requests,time
from requests.models import Response
import pandas as pd
import os.path

# Creamos las diferentes listas que se irán alimentando

lista_general = list()
lista_homer = list()
lista_lisa = list()
recuento_palabras = {}

def obtener_quote():

  URL ='https://thesimpsonsquoteapi.glitch.me/quotes'
  respuesta :Response = requests.get(url = URL)

  # Extraemos los datos en formato JSON

  datos = respuesta.json()

  # Obtenemos valor de la frase y el nombre en la claves del JSON que nos interesa

  s_quote = datos[0]
  quote = s_quote['quote']
  name = s_quote['character']
  image = s_quote['image']

  # Especificamos la ruta de la carpeta del personaje

  path = "app/Imagenes/" + name

  # Verificamos si la carpeta del personaje está creada y sino la crea

  carpeta_personaje = os.path.exists(path)
  if carpeta_personaje == False:
   os.mkdir(path)
  
  # Guardamos la imagen en la carpeta del personaje

  image_name = "app/Imagenes/" + name + "/"+ name + ".png"
  imagen = requests.get(image).content
  with open(image_name, 'wb') as file:
    file.write(imagen)

  # Quitamos signos de puntuación para el recuento de palabras

  sigpunt = str.maketrans("","", string.punctuation)
  del sigpunt[ord("'")]

  # Guardamos en una lista el recuento de palabras

  def recuento(recuento_palabras):

    palabras_frase = quote.split()
    
    for palabra in palabras_frase:
      palabra = palabra.translate(sigpunt).lower()
      if palabra in recuento_palabras:
        recuento_palabras [palabra] += 1
      else:
        recuento_palabras [palabra] = 1
    return recuento_palabras  

  print(recuento(recuento_palabras))

  # Guardamos la lista en un fichero csv

  file_recuento = pd.DataFrame.from_dict(recuento_palabras, orient='index')
  file_recuento.to_csv('app/Palabras.csv', mode='wb', header=False)

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