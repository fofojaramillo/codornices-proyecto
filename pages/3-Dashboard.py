import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import matplotlib.dates as mdates


st.title('Explorando los datos de la Codorniz Moctezuma')

# Lectura de datos
df = pd.read_csv('./data/processed/dataset_preprocessed.csv')


#----------------------------------------------------------------------------------------------------------------------
# st.subheader('Ubicación de Codornices')

# Crear un mapa centrado en una ubicación inicial (latitud y longitud promedio)
mapa = folium.Map(location=[df['lat'].mean(), df['lon'].mean()], zoom_start=5)

# Crear un cluster de marcadores para gestionar muchos marcadores en el mapa
marker_cluster = MarkerCluster().add_to(mapa)

# Iterar sobre cada fila del DataFrame y agregar un marcador al cluster para cada punto
for index, row in df.iterrows():
    # Obtener la latitud y longitud de la fila actual
    lat, lon = row['lat'], row['lon']
    # Crear un marcador y agregarlo al cluster en el mapa
    folium.Marker([lat, lon], popup=f"ID: {row['id']}, Estado: {row['estado']}, Peso total: {row['peso total']}").add_to(marker_cluster)

# Mostrar el mapa en la aplicación de Streamlit
folium_static(mapa)




# st.subheader('Total de registros')

# Widget para seleccionar la columna
columna_seleccionada = st.selectbox('Cantidad de registros por:', ['Estado', 'Sexo', 'Edad'], index=0, key='select_columna')

# Convertir la selección a minúsculas
columna_seleccionada_lower = columna_seleccionada.lower()

# Calcular la suma por cada valor en la columna seleccionada
suma_por_columna = df[columna_seleccionada_lower].value_counts().reset_index()
suma_por_columna.columns = [columna_seleccionada_lower, 'counts']

# Establecer estilo de seaborn
sns.set(style="whitegrid")

# Graficar la suma por columna
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=suma_por_columna, x=columna_seleccionada_lower, y='counts',hue=columna_seleccionada_lower, dodge=False, palette='viridis', ax=ax, legend=False)

# Ajustar la rotación de las etiquetas del eje x
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')  # Rotar las etiquetas a 45 grados hacia la derecha
ax.set_xlabel(columna_seleccionada.capitalize(), fontsize=12)  # Establecer etiqueta del eje x
ax.set_ylabel('Número de registros', fontsize=12)  # Establecer etiqueta del eje y
ax.set_title(f'Registros por {columna_seleccionada.capitalize()}', fontsize=16)  # Agregar título con formato

# Añadir etiquetas de valores en cada barra
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

st.pyplot(fig)










#----------------------------------------------------------
st.subheader('Peso total en el buche de codornices por estado')


# Convertir la columna 'time' a formato datetime
df['time'] = pd.to_datetime(df['time'], format='%H:%M')

# Ordenar el DataFrame por la columna 'time'
df.sort_values(by='time', inplace=True)

# Widget de selección para el degradado de color
color_by = st.selectbox('Peso total vs Tiempo vs:', ['Precipitación', 'Temperatura', 'Altitud'], index=0)

# Mapeo de opciones a columnas
color_by_map = {
    'Precipitación': 'ppanual17',
    'Temperatura': 'tmedia17',
    'Altitud': 'altitud'
}

# Columna seleccionada para el degradado de color
color_column = color_by_map[color_by]

# Widget de selección para el filtro de tiempo
time_filter = st.selectbox('Filtro de tiempo:', ['Historico', 'Antes de las 13:00', 'Después de las 13:00'], index=0)

# Función para aplicar el filtro de tiempo
def aplicar_filtro_tiempo(df, filtro):
    if filtro == 'Antes de las 13:00':
        return df[df['time'] < pd.to_datetime('13:00', format='%H:%M')]
    elif filtro == 'Después de las 13:00':
        return df[df['time'] >= pd.to_datetime('13:00', format='%H:%M')]
    else:
        return df

# Aplicar el filtro de tiempo a los datos
df_all_filtrado = aplicar_filtro_tiempo(df, time_filter)

# Filtrar datos por estado
df_az = df_all_filtrado[df_all_filtrado['estado'] == 'AZ']
df_nm = df_all_filtrado[df_all_filtrado['estado'] == 'NM']

# Obtener el rango de color para el degradado
color_range = (min(df_all_filtrado[color_column]), max(df_all_filtrado[color_column]))

# Crear figuras y ejes para las gráficas
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# Función para crear la gráfica
def crear_grafica(data, estado, color_by, ax):
    # Crear una paleta de colores
    palette = sns.color_palette('viridis', as_cmap=True)

    # Graficar los datos
    scatter = ax.scatter(data['time'], data['peso total'], c=data[color_by], cmap=palette, s=50, vmin=color_range[0], vmax=color_range[1])

    # Configurar la periodicidad de las etiquetas del eje x
    ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=15))  # Cada 15 minutos
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

    # Configurar el rango del eje y para que sea el mismo en ambas gráficas
    ax.set_ylim(min(df_all_filtrado['peso total']), max(df_all_filtrado['peso total']))

    # Rotar las etiquetas del eje x
    ax.tick_params(axis='x', rotation=45)

    # Agregar una barra de color
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label(color_by)

    # Configurar etiquetas y título
    ax.set_xlabel('Hora')
    ax.set_ylabel('Peso Total')
    ax.set_title(f'Peso Total del buche de las codornices por {color_by} en {estado}')

# Crear y mostrar gráficas para cada estado
crear_grafica(df_az, 'AZ', color_column, axs[0])
crear_grafica(df_nm, 'NM', color_column, axs[1])

# Ajustar diseño y mostrar la figura
plt.tight_layout()
st.pyplot(fig)


#-----------------------------------------------------------------------
columns = list(df.columns)
df_dieta = df[columns[6:-11]].copy()

# # Calcular los porcentajes para cada columna
# column_percentages = df_dieta.sum() / df_dieta.sum().sum()

# # Filtrar los alimentos que tienen al menos el 5% de la proporción
# column_percentages_filtered = column_percentages[column_percentages >= 0.05]

# # Calcular el porcentaje total de "Otros"
# otros_percentage = 1 - column_percentages_filtered.sum()

# # Crear un nuevo DataFrame con los alimentos que cumplen el criterio y "Otros"
# df_plot = pd.concat([column_percentages_filtered, pd.Series({'Otros': otros_percentage})])

# # Ordenar los porcentajes de mayor a menor
# df_plot_sorted = df_plot.sort_values(ascending=True)


# # Añadir etiquetas y título
# st.subheader('Proporciones de Alimentos (>= 5%) y Otros')
# # Crear la gráfica de barras con Streamlit
# st.bar_chart(df_plot_sorted)






# Calcular los porcentajes para cada columna
column_percentages = df_dieta.sum() / df_dieta.sum().sum()

# Filtrar los alimentos que tienen al menos el 5% de la proporción
column_percentages_filtered = column_percentages[column_percentages >= 0.05]

# Calcular el porcentaje total de "Otros"
otros_percentage = 1 - column_percentages_filtered.sum()

# Crear un nuevo DataFrame con los alimentos que cumplen el criterio y "Otros"
df_plot = pd.concat([column_percentages_filtered, pd.Series({'Otros': otros_percentage})])

# Ordenar los porcentajes de mayor a menor
df_plot_sorted = df_plot.sort_values(ascending=True)

# Añadir etiquetas y título
st.subheader('Proporciones de Alimentos (>= 5%) y Otros')

# Crear la gráfica de barras con Streamlit
fig, ax = plt.subplots()
bars = ax.barh(df_plot_sorted.index, df_plot_sorted.values * 100, height=0.8)  # Multiplicar por 100 para obtener el porcentaje en lugar de la fracción

# Ajustar el espacio entre las etiquetas y las barras
plt.yticks(fontsize=10)  # Ajustar el valor de pad según sea necesario

# Agregar los porcentajes al final de cada barra
for bar, percentage in zip(bars, df_plot_sorted.values * 100):
    ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{percentage:.1f}%', ha='left', va='center')

# Añadir etiquetas y título al gráfico
ax.set_xlabel('Porcentaje (%)')
ax.set_ylabel('Alimentos')
# ax.set_title('Proporciones de Alimentos (>= 5%) y Otros')

# Mostrar la gráfica en Streamlit
st.pyplot(fig)