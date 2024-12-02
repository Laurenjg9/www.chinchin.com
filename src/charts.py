import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo JSON
df = pd.read_json("Respuesta_form.json")

# Seleccionar las columnas necesarias
columna_edad = "Por favor, indica tu edad"
columna_deuda = "¿Tienes alguna deuda activa en este momento? [SI]"

# Reemplazar valores faltantes o inconsistentes
df[columna_deuda] = df[columna_deuda].fillna("No tiene deudas")

# Contar las edades por tipo de deuda
conteo_edades_por_deuda = df.groupby([columna_deuda, columna_edad]).size().unstack(fill_value=0)

# Crear el gráfico
conteo_edades_por_deuda.plot(kind="barh", figsize=(10, 6), stacked=True, cmap="tab20c")

# Personalizar el gráfico
plt.title("Relación entre tipos de deudas y rango de edad")
plt.xlabel("Número de personas")
plt.ylabel("Tipos de deudas activas")
plt.legend(title="Rangos de edad", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

# Mostrar el gráfico
plt.show()
plt.savefig("grafica.png")
plt.close()