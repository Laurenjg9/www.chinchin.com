import json
import csv
import os

# Ruta del directorio donde se guardara el archivo JSON
directory = os.getcwd()
print(f"este es la ruta: {directory}\n")
# Validacion de que la nueva carpeta "directory" no exsista
os.makedirs(directory, exist_ok = True)      #si no, que la cree
# Creacion del archivo e indicacion donde la guardara

file_path = os.path.join(directory, "Nuevo_Archivo.json") # Marvelianos1 es el nombre del archivo


#TRANSFORMACION ARCHIVO CSS A JSON

with open("Estudio de mercado.csv", 'r') as archivo: # 1. ABRIR EL ARCHIVO Y LEERLO
    lector = csv.DictReader(archivo, delimiter=";")  # 2. CONVERTIRLO A DICCIONARIO
    datos = [fila for fila in lector]

    #print(f"\nImprimiendo diccionario:\n{datos}\n")
    
    # 2.1. VERIFICANDO VALORES
    """for i in range(0,len(datos)):      # For para que recorra e imprima linea por linea
        print(f"\nPersonaje #{i+1}:\n")
    
    for key in datos[i].keys():    # For para que recorra dentro de la linea las claves y valores
        print(f"{key}: {datos[i][key]}")"""
    
    
# 3. GUARDAR EN UN ARCHIVO JSON

with open("Encuesta.json","w") as archivo_json:
    json.dump(datos, archivo_json, indent=4, ensure_ascii=False)

print(f"\nDiccionario nuevo agregado a: {file_path}")

