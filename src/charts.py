import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde el JSON
df = pd.read_json("Respuesta_form.json")


# Análisis 1: Rango de edad vs Gastos

# Columnas relevantes
columna_edad = "Por favor, indica tu edad"
categorias_gasto = [
    "Ingresos destinados a Deudas y créditos",
    "Ingresos destinados a Alimentación",
    "Ingresos destinados a Pagos de servicios domésticos"
]

# Conversión de rangos a valores numéricos
conversion_porcentajes = {
    "No aplica": 0,
    "Menos del 10%": 5,
    "Entre el 10% y el 20%": 15,
    "Entre el 20% y el 40%": 30,
    "Entre el 40% y el 50%": 45,
    "Entre el 50% y el 70%": 60,
    "Entre el 70% y el 100%": 85
}

# Aplicar conversión
for categoria in categorias_gasto:
    df[categoria] = df[categoria].map(conversion_porcentajes)

# Agrupar por rango de edad y calcular promedios
promedios_por_edad = df.groupby(columna_edad)[categorias_gasto].mean()

# Crear el gráfico
promedios_por_edad.plot(kind="bar", figsize=(10, 6), stacked=True, cmap="viridis")
plt.title("Ingresos destinados a gastos por rango de edad")
plt.xlabel("Rango de edad")
plt.ylabel("Porcentaje promedio (%)")
plt.legend(title="Categorías de gasto", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

#crear imagen
plt.savefig("1.destino_ingresos_rango_edad.png")
plt.show()

# Análisis 2: Deudas por rango de edad

# Columnas relacionadas con las deudas
columnas_deudas = [
    "Deuda Tarjetas de crédito",
    "Deuda Créditos de libre inversión",
    "Deuda Créditos de vivienda o vehículo",
    "Deuda Crédito educativo",
    "Deuda Préstamos con gota a gota",
    "Deuda Préstamos de amistades, familiares, etc.",
    "Deuda No tengo deudas activas"
]

# Agrupar por edad y sumar las deudas
deudas_por_edad = df.groupby(columna_edad)[columnas_deudas].sum()

# Crear el gráfico
deudas_por_edad.plot(kind="bar", figsize=(12, 6), stacked=True, cmap="tab20c")
plt.title("Tipos de deudas por rango de edad")
plt.xlabel("Rango de edad")
plt.ylabel("Número de personas")
plt.legend(title="Tipos de deudas", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

#crear imagen
plt.savefig("2.Deudas_rango_edad.png")
plt.show()

# 3 Educacion ahorro vs rango edad

# Columnas relacionadas con formas de aprender
formas_aprender = [
    "Participando en talleres o cursos presenciales",
    "A través de videos educativos y paginas web",
    "Recibiendo asesorías personalizadas con expertos",
    "Mediante juegos o actividades interactivas sobre ahorro"
]

# Sumar el total de selecciones para cada forma de aprender
totales_aprender = df[formas_aprender].sum()

#totales_aprender.index = [label.replace(", ", ",\n") for label in totales_aprender.index]
# Crear el gráfico de torta
plt.figure(figsize=(8, 8))
totales_aprender.plot(
    kind="pie",
    autopct='%1.1f%%',  # Mostrar porcentajes
    startangle=90,      # Comenzar desde arriba
    cmap="Set3",        # Colores agradables
    ylabel=""           # Quitar etiqueta del eje Y
)

plt.title("Proporción general de preferencias sobre formas de aprender ahorro")
plt.tight_layout()
plt.savefig("3.grafico_torta_aprender.png", dpi=300, bbox_inches='tight')  # Guardar el gráfico
plt.show()