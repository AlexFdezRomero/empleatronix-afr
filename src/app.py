import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd 

st.title("EMPLEATRONIX - ALEJANDRO FR")

st.write("Todos los datos sobre los empleados en una aplicación:")

# Carga de datos
path = "/data/employees.csv"

df = pd.read_csv(path)

# Muestra de los datos
st.dataframe(df)

st.divider()

col1, col2, col3 = st.columns([1,1,1])

with col1:
    # Elección de color
    muestra_color = st.color_picker('Elige un color para las barras', '#3475B3')
with col2:
    # Botón para mostrar el nombre en la gráfica
    muestra_nombre = st.toggle('Mostrar el nombre', value=1)
with col3:
    # Botón para mostrar el sueldo en la gráfica
    muestra_sueldo = st.toggle('Mostrar sueldo en la barra')
    
# Mostrar la gráfica
nombre = df["full name"]
sueldo = df["salary"]

fig, ax = plt.subplots()
bars = ax.barh(nombre, sueldo, color=muestra_color)

if muestra_sueldo:
    ax.bar_label(container=bars, fmt="%d€")

if not muestra_nombre:
    plt.yticks([])

plt.xticks(rotation=90)

plt.xlim([0, 4500])

st.pyplot(fig)