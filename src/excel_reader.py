import openpyxl
import pandas as pd

# 1. LECTURA DEL ARCHIVO DE EXCEL
file_reader = pd.read_excel("Form_Prueba.xlsx")
#print(file_reader.head())       # Mostrar la cabecera del archivo

# 2. CONVERTIR A JSON
file_reader.to_json("Form_excel.json",orient="records", indent=4)
print("Archivo Json generado exitosamente")