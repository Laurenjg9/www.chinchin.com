import pandas as pd
import matplotlib.pyplot as plt

# Cargar archivo JSON
df = pd.read_json("Respuesta_Form.json")

# Definir las columnas de interés
columna_edad = "Por favor, indica tu edad"
categorias_gasto = [
    "¿Qué porcentaje de tus ingresos mensuales destinas para cubrir los siguientes gastos?\n [Deudas y créditos]",
    "¿Qué porcentaje de tus ingresos mensuales destinas para cubrir los siguientes gastos?\n [Alimentación]",
    "¿Qué porcentaje de tus ingresos mensuales destinas para cubrir los siguientes gastos?\n [Pagos de servicios domésticos]",
    "¿Qué porcentaje de tus ingresos mensuales destinas para cubrir los siguientes gastos?\n [Alquiler de vivienda]",
    "¿Qué porcentaje de tus ingresos mensuales destinas para cubrir los siguientes gastos?\n [Transporte]",
    "¿Qué porcentaje de tus ingresos mensuales destinas para cubrir los siguientes gastos?\n [Ocio y entretenimiento]",
]

# Diccionario para convertir textos a valores numéricos
conversion_porcentajes = {
    "No aplica": 0,
    "Entre el 10% y el 20%": 15,
    "Entre el 20% y el 40%": 30,
    "Entre el 40% y el 50%": 45,
    "Entre el 50% y el 70%": 60,
    "Entre el 70% y el 100%": 85,
}

# Convertir categorías de gasto a valores numéricos
for categoria in categorias_gasto:
    df[categoria] = df[categoria].map(conversion_porcentajes)

# Agrupar por rango de edad y calcular promedios
promedios_gasto_por_edad = df.groupby(columna_edad)[categorias_gasto].mean()

# Crear el gráfico de barras apiladas
promedios_gasto_por_edad.plot(kind="bar", figsize=(12, 8), stacked=True, cmap="tab20c")

# Personalizar el gráfico
plt.title("Promedio de gastos mensuales por categoría y rango de edad", fontsize=14)
plt.xlabel("Rango de edad", fontsize=12)
plt.ylabel("Porcentaje promedio (%)", fontsize=12)
plt.legend(title="Categorías de gasto", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

# Mostrar el gráfico
plt.show()

"""import pandas as pd
import numpy as np
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

#crear imagen
plt.savefig("grafico_deudas_edad.png")"""