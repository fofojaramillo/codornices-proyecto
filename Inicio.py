import streamlit as st
import pandas as pd
import numpy as np

# st.title('Análisis estadístico sobre la composición de la dieta de la codorniz moctezuma y su relación con la diversidad y abundancia de la especie')
st.title("ANÁLISIS ESTADÍSTICO SOBRE LA COMPOSICIÓN DE LA DIETA DE LA CODORNIZ MOCTEZUMA Y SU RELACIÓN CON LA DIVERSIDAD Y ABUNDANCIA DE LA ESPECIE")

st.divider()

st.subheader('Introducción')
introduccion = '''
En ecología podemos agrupar las distintas especies en dos categorías: generalistas
 y especialistas. Las especies generalistas son aquellas capaces de habitar distintos biomas
 (esto es, grandes unidades ecológicas con condiciones ambientales concretas), mientras
 que las especialistas solo pueden adaptarse a un solo bioma o conjunto de condiciones.
 Ante esto, la capacidad de supervivencia de este último grupo puede verse afectada por
 distintos factores ambientales, provocando así en muchos casos la disminución de su
 población.
 
 En las últimas décadas las codornices norteamericanas han presentado bajas en
 sus poblaciones. Esto se le atribuye a distintos factores climatológicos y humanos, entre
 ellos, el aumento de la temperatura media, cambio de los patrones de precipitación y la
 cacería, los cuales se creen que afectan la disponibilidad y cantidad de alimentos, sobre
 todo en las zonas más áridas. Estos cambios a su vez pueden cambiar los hábitos de
 forrajeo de la fauna silvestre, esto para cumplir con requisitos de crecimiento, reproducción
 y supervivencia.

 El estudiante de doctorado Óscar López Bujanda tiene como objetivo analizar la
 variación de la composición de la dieta invernal de la codorniz moctezuma (una especie de
 codorniz que es considerada especialista) en Arizona y Nuevo México, considerando 324
 buches de codornices cosechadas entre los años 2009 y 2017 y relacionando los datos
 obtenidos con otras características ambientales, como la temperatura y la precipitación. Con
 toda esta información, se busca aceptar o rechazar la hipótesis de que la variabilidad de la
 dieta del ave es en efecto, influenciada por factores climáticos, geográficos y ecológicos.
 Con el fin de contribuir con el objetivo anterior, ProData Analytics Consultores busca
 analizar con distintas técnicas estadísticas la dieta de la codorniz, comenzando con un
 análisis descriptivo fundamental. Posteriormente, se buscará realizar técnicas y métodos
 más específicos como pruebas de hipótesis y análisis de grupos, proveyendo así un mayor
 entendimiento de cómo las distintas variables ambientales tienen un impacto tanto en la
 composición de la dieta de la codorniz, como en los distintos índices de diversidad.

 El alcance del proyecto es realizar un análisis estadístico de los datos
 proporcionados, así como la entrega de reportes formales y presentaciones ejecutivas,
 dando en la finalización del mismo un reporte interactivo con resumen de resultados.
'''
st.markdown(f'<div style="text-align: justify">{introduccion}</div>', unsafe_allow_html=True)


st.divider()
st.caption('Integrantes:')
data = '''
- Luís Andrés Burruel Durán
- Rodolfo Armando Jaramillo Ruíz
- Estephania Pivac Alcaraz
- Vesna Camile Pivac Alcaraz
- Guillermo Velazquez Coronado
'''
st.caption(data)
