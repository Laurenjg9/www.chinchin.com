import openpyxl
import pandas as pd

# 1. LECTURA DEL ARCHIVO DE EXCEL
file_reader = pd.read_excel("Respuestas_Form.xlsx")
#print(file_reader.head())       # Mostrar la cabecera del archivo

# 2. CONVERTIR A JSON
file_reader.to_json("Respuesta_form.json",orient="records", force_ascii=False, indent=4)
print("Archivo Json generado exitosamente")
