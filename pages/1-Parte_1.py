import streamlit as st
import pandas as pd 

st.title('Acuerdo de Servicios de Consultoría Estadística')


st.divider()

st.subheader("Objetivos, metas, estrategias y acciones")
    
objetivos = ''' 
Objetivos:
 - Estimar los patrones de abundancia de la codorniz.
 - Analizar la variación de la dieta de la codorniz a través de su distribución.
 - Analizar la variación de la dieta y abundancia a partir de factores externos.
 '''

st.markdown(objetivos)


data = {
    'Fase': [1, 2],
    'Objetivo': ['''1.- Revisión de la tesis que contiene el trabajo terminal de maestría del cliente, así como las referencias más relevantes.\n
2.- Revisión exploratoria de la base de datos sobre características de alimentación de la codorniz moctezuma.\n
3.- Limpieza de datos y otros ajustes relacionados a los mismos.\n
4.- Tratamiento de outliers.\n
5.- Elaboración del análisis exploratorio de los datos.''',
                 '''1.- Realización de distintas pruebas de hipótesis y análisis de grupos, así como otras herramientas estadísticas pertinentes.\n
2.- Análisis de las variables que más tienen influencia sobre la diversidad y abundancia.'''],
    'Meta': ['''1.- Reporte formal de resultados obtenidos con estadística descriptiva.\n
2.- Presentación de los resultados.\n
3.- Delimitar las herramientas, técnicas y metodologías más adecuadas a utilizar en la siguiente fase de acuerdo a los datos proporcionados, así como identificar limitaciones y líneas de acción.''',
             '''1.- Reporte formal con resultados obtenidos.\n
2.- Herramienta interactiva de visualización de resultados.\n
3.- Presentación de los resultados.'''],
    'Estrategia': ['''1.- Entender la problemática a abordar e investigar sobre el estado del arte para determinar las herramientas adecuadas a utilizar.\n
2.- Explorar los datos proporcionados por Oscar para identificar desafíos, así como realizar la limpieza adecuada para la siguiente fase.''',
                   '''1.- Identificar los grupos de alimentación más significativos para la especie para realizar las pruebas de hipótesis.\n
2.- Selección de características de variables para la realización de los análisis de grupos.'''],
    'Acción': ['''1.- Investigar antecedentes del problema a abordar.\n
2.- Reuniones periódicas con Oscar.\n
3.- Utilizar software estadístico (Python / R) para la elaboración del procesamiento y análisis exploratorio.\n
4.- Elaboración de los entregables.''',
               '''1.- Reuniones periódicas con Oscar.\n
2.- Utilizar software estadístico para la elaboración de pruebas y análisis.\n
3.- Utilizar PowerBi para la elaboración de una herramienta de visualización interactiva.\n
4.- Realizar entregables.''']
}

df = pd.DataFrame(data)

# Mostrar la tabla en Streamlit sin el índice
st.table(df.set_index('Fase', drop=True))


st.subheader('Planificación de secuencia de trabajo')

# Define los datos de la tabla
data = {
    'Fase': [1,2],
    'Observaciones': ['Incluye entregables', 'Incluye entregables'],
    'Semana 1': ['x', ''],
    'Semana 2': ['x', ''],
    'Semana 3': ['', 'x'],
    'Semana 4': ['', 'x'],
    'Semana 5': ['','x'],
    'Semana 6': ['','x'],
}

# Crea un DataFrame a partir de los datos
df = pd.DataFrame(data)

# Crea la interfaz de Streamlit
st.write(df.set_index('Fase', drop=True))


st.subheader('Equipo de trabajo')
data = {
    'Miembro del Equipo': [
        'Lic. Luis Andrés Burruel Durán', 
        'M.Sc. Estephania Pivac Alcaraz', 
        'Lic. Vesna Camile Pivac Alcaraz', 
        'Lic. Rodolfo Armando Jaramillo Ruiz', 
        'Lic. Guillermo Velazquez Coronado', 
        'M.Sc. Oscar Enrique López Bujanda'
    ],
    'Cargo/Actividad': [
        'Implementación de métodos relacionados a reducción de dimensionalidad y análisis de grupos', 
        'Responsable del análisis estadístico: pruebas de hipótesis e inferencia. Desarrollo en PowerBi.', 
        'Desarrollo de entregables y código para implementación de métodos estadísticos y analíticos.', 
        'Análisis estadístico y exploratorio de datos.', 
        'Desarrollo de entregables y código para la obtención de resultados.', 
        'Experto en el tema'
    ],
    'Observaciones': [
        'Licenciatura en Matemáticas, actualmente cursando la Maestría en Ciencia de Datos', 
        'Maestría en Ciencias Matemáticas, actualmente cursando la Maestría en Ciencia de Datos', 
        'Licenciatura en Ciencias de la Computación, actualmente cursando la Maestría en Ciencia de Datos', 
        'Licenciatura en Física, actualmente cursando la Maestría en Ciencia de Datos', 
        'Licenciatura en Ciencias de la Computación, actualmente cursando la Maestría en Ciencia de Datos', 
        'Maestría en Biociencias, actualmente cursando el Doctorado en Biociencias'
    ],
    'LinkedIn': [
        '@andresburruel', 
        '@estephaniapivac', 
        '@vesna-pivac', 
        '@rodolfojaramillo', 
        '@guillermovc', 
        '@oscarlópez'
    ]
}

# Crea un DataFrame a partir de los datos
df = pd.DataFrame(data)

# Crea la interfaz de Streamlit
st.table(df)



st.subheader('Requerimientos')
st.markdown('Bases de datos, documentación y artículos requeridos para la elaboración del proyecto.')

st.subheader('Entregables')
st.markdown('''
- Reportes formales con resultados
- Presentación ejecutiva con los resultados
- Reporte interactivo con resumen de resultados
            ''')


st.subheader('Presupuesto')
st.markdown('El costo total de los servicios (en moneda nacional) se presenta en la siguiente tabla:')

data = {
    'Concepto': [
        'Pago Primera Fase', 
        'Pago Segunda Fase', 
        'Software (PowerBI) por año', 
        'Recursos adicionales', 
        'Total'
    ],
    'Monto': [
        '180,000.00', 
        '276,000.00', 
        '2,532.00 por año', 
        '15,000.00', 
        '473,532.00'
    ]
}

# Crea un DataFrame a partir de los datos
df_costos = pd.DataFrame(data)

# Crea la interfaz de Streamlit
st.table(df_costos)