import streamlit as st
import pandas as pd

st.title('Reporte de Resultados')

st.divider()


# Índice en la barra lateral
st.sidebar.caption('Índice')


# Enlaces a los subencabezados
st.sidebar.markdown('[Normalidad y medias entre estados](#normalidad-y-medias-entre-estados)')
st.sidebar.markdown('[Reducción de dimensionalidad](#4ce38ab2)')
st.sidebar.markdown('[Análisis de condiciones climatológicas entre estados](#194f6b63)')
st.sidebar.markdown('[Regresión de Dirichlet](#bb30fdeb)')
st.sidebar.markdown('[Prueba de diferencia de medias: ANOVA](#prueba-de-diferencia-de-medias-anova)')
st.sidebar.markdown('[Modelos Lineales Generalizados (GLM): Poisson](#modelos-lineales-generalizados-glm-poisson)')







st.subheader('Normalidad y medias entre estados')
normmedias=('''Con la intención de hacer pruebas de medias entre diferentes grupos para el peso total del buche y la diversidad del ambiente (hcrop) se hicieron pruebas de hipótesis para ver la evidencia a favor de que la distribución de estas variables fuera en primera instancia normal o, en su defecto, lognormal. Después de realizar la prueba de Shapiro-Wilk para el log de las variables (ya que las variables no se apreciaban normales en sus gráficas) se llegó a un rechazo de la hipótesis de que la muestra venía de una distribución normal. Se trataron otras pruebas que llegaron a la misma conclusión.
Por lo anterior se procedió con una prueba no paramétrica, la prueba de Mannwhitneyu. \n
            
Por estados, se llegó a que la prueba para este muestra no rechazaba la hipótesis de que las medias del peso del buche no difieren entre Arizona y Nuevo México. Mientras que la diversidad del ambiente sí difiere en sus medias según esta prueba. Mientras que por edad, la prueba no rechaza que las medias difieran. Mientras que para las codornices cosechadas antes de las 13:00 hrs y las cosechadas después de esta hora, las medias difieren tanto para el peso del buche como la diversidad del ambiente. Lo anterior parece indicar que hay evidencia que podría apuntar a cómo varía el comportamiento de las codornices en cuanto su alimentación.''')

st.markdown(f'<div style="text-align: justify">{normmedias}</div>', unsafe_allow_html=True)




st.subheader("Reducción de dimensionalidad")
reduccion_dimensionalidad= '''
Se aplicó la técnica t-SNE de reducción de dimensionalidad en dos subconjuntos de datos. El primer subconjunto eran básicamente todas las variables numéricas, eliminando datos como la edad, estado o id de la codorniz, y otro tenía solamente las variables relacionadas con los alimentos y el peso del buche. En el primer subconjunto se obtuvo un mapeo de reducción de dimensionalidad interesante, el cual mostramos a continuación:
'''
st.markdown(f'<div style="text-align: justify">{reduccion_dimensionalidad}</div>', unsafe_allow_html=True)
st.image('./images/t-SNE.png', width=400,caption='t-SNE')
st.markdown("En este parecen haber dos grupos de datos. En efecto, al realizar el algoritmo de Kmeans con 2 grupos se obtiene lo siguiente:")
st.image('./images/kmeans.png', width=400,caption='Kmeans')
rd_2='''Al momento de comparar las etiquetas asignadas para cada dato, se obtiene que estás coinciden con el estado aproximadamente un 95% de las veces, habiendo en la categoría 0 124 muestras exclusivamente de Nuevo México, mientras que en la categoría 1 hay 85 registros de Arizona y 11 de Nuevo México. Luego, se creó un árbol de decisión para poder predecir la categoría asignada por el algoritmo de Kmeans.
    '''
st.markdown(f'<div style="text-align: justify">{rd_2}</div>',unsafe_allow_html=True)
st.image('./images/desitiontree.png', width=500,caption='Arbol de decisión')
rd_3='''
Observemos que en los primeros nodos del diagrama anterior observamos variables climatológicas. Ante esto, se piensa que los clusters son generados por la diferencia de esas variables. Por otro lado, para el segundo subconjunto de datos se obtuvo el siguiente mapeo de reducción de dimensionalidad:
'''
st.markdown(f'<div style="text-align: justify">{rd_3}</div>',unsafe_allow_html=True)
st.image('./images/rd.png', width=500,caption='Reducción de dimencionalidad en base al árbol de decisión.')
rd_4='''En este caso, no se identificaron agrupamientos en los datos.

Así, se tienen indicios de que los datos tienen una separación o se agrupan más por estado utilizando variables climatológicas o ambientales.'''
st.markdown(f'<div style="text-align: justify">{rd_4}</div>',unsafe_allow_html=True)




st.subheader('Análisis de condiciones climatológicas entre estados')
CE = '''
El problema expuesto en este proyecto intenta determinar si podemos encontrar indicios de que las condiciones o cambios climatológicos inducen una alteración en la dieta de la Codorniz Moctezuma. Ante esto, se planea utilizar estos dos estados como grupos, ver si se pueden diferenciar en variables como temperatura media y precipitación, y ver si existe variación en índices como la diversidad del buche y la diversidad del entorno.

Realizando una gráfica de temperatura media y precipitación, se obtuvo lo siguiente: 
'''
st.markdown(f'<div style="text-align: justify">{CE}</div>',unsafe_allow_html=True)
st.image('./images/temp-pp.png', width=500,caption='Temperatura y precipitación')
CE2='''
Podemos observar que ambos estados se pueden diferenciar bien, siendo los datos en amarillo los de Nuevo México, y los otros los de Arizona. Se puede apreciar también que existe una mayor variación tanto de temperatura media como de precipitación en el primer estado. 
En cuanto a la altitud, se obtuvo la siguiente gráfica:
'''
st.markdown(f'<div style="text-align: justify">{CE2}</div>',unsafe_allow_html=True)
st.image('./images/Altitud-PP.png', width=500,caption='Altitud y precipitación')
CE3='''
en la cual también podemos apreciar diferencias entre ambos estados. Así, se puede pensar que ambos estados se pueden distinguir bien basándonos en estas tres variables climatológicas. Para tener más evidencia, se realizaron pruebas de permutación. En nuestras pruebas, y tomando el estadístico de la media muestral, nuestra hipótesis nula fue que la media de estas tres variables entre estados eran iguales con un nivel de significancia de = 0.05, y la hipótesis alternativa fué que la media era menor o mayor, dependiendo del signo de la diferencia de medias de la variable. 
Utilizando 100 remuestreos en la prueba, se obtuvieron los siguientes resultados:
'''
st.markdown(f'<div style="text-align: justify">{CE3}</div>',unsafe_allow_html=True)
st.image('./images/permutacion.png', width=500,caption='Pruebas de permutación')
CE4='''
Debido a que los tres p-valores fueron menores a , se tiene evidencia para rechazar la hipótesis nula, y aceptar la hipótesis alternativa en cada caso. Finalmente, se calculó la media de los índices de diversidad, y se consiguió lo siguiente:
'''
st.markdown(f'<div style="text-align: justify">{CE4}</div>',unsafe_allow_html=True)
st.image('./images/mediaDiv.png', width=500,caption='Media de los índices de diversidad.')
st.markdown('Resulta interesante ver que Arizona tiene evidencia de tener mayor temperatura media y precipitación y mayores índices de diversidad.')




st.subheader("Regresión de Dirichlet")
D0 = '''
Para poder observar si la dieta de la codorniz es influenciada por factores ambientales, se le pidió al cliente que agrupara los alimentos que más frecuentemente consume la codorniz en los llamados grupos funcionales. Los grupos definidos fueron:

- Temperatura baja y alta precipitación (tbap)
- Temperatura baja y baja precipitación (tbbp)
- Temperatura alta y alta precipitación (taap)
- Temperatura alta y baja precipitación (tabp)

Para poder realizar la regresión de Dirichlet, se formaron estos cuatro grupos y se normalizaron con respecto a su suma. Se obtuvieron las siguientes proporciones de los grupos en la dieta de la codorniz.
'''
st.markdown(f'<div style="text-align: justify">{D0}</div>',unsafe_allow_html=True)
st.image('./images/proporcion_grupos_fun_dieta.png', width=500,caption='Proporción de grupos funcionales en la dieta.')
D1 = '''Adicionalmente, se hicieron seis subconjuntos de datos, los datos originales, dos subconjuntos considerando el estado, y otros cuatro basándonos en el estado y si la muestra se tomó antes o después de las 13:00. 

Los subconjuntos con resultados más significativos fueron los siguientes:'''
st.markdown(f'<div style="text-align: justify">{D1}</div>',unsafe_allow_html=True)
st.markdown('<div style="text-align: center"><b>Conjunto de datos total</b></div>',unsafe_allow_html=True)
st.image('./images/subconjunto-total.png', width=500,caption='Subconjunto de datos total')
st.markdown('<div style="text-align: center"><b>Datos de Arizona</b></div>',unsafe_allow_html=True)
st.image('./images/subconjunto-arizona.png', width=500,caption='Subconjunto de datos de Arizona')
st.markdown('<div style="text-align: center"><b>Datos de Arizona después de las 13:00</b></div>',unsafe_allow_html=True)
st.image('./images/subconjunto-az-13.png', width=500,caption='Subconjunto de datos de Arizona después de las 13:00h')
D2='''El grupo funcional donde se obtuvieron p-valores más significativos (tomando un = 0.05) fue Temperatura baja y alta precipitación (tbap). En las tres regresiones mostradas, resulta interesante el hecho de que a la variable tmedia17 (temperatura media) se le asigna un coeficiente negativo.'''
st.markdown(f'<div style="text-align: justify">{D2}</div>',unsafe_allow_html=True)


st.subheader("Prueba de diferencia de medias: ANOVA")
anova='''Se realizó una prueba ANOVA para evaluar las posibles diferencias en la diversidad dentro del buche (hcrop) entre estados y/o los grupos formados. Los resultados indicaron un p-valor menor al 5%, lo que sugiere una diferencia significativa. Sin embargo, los análisis post-hoc revelaron que esta diferencia significativa se observa principalmente entre las medias de hcrop de los diferentes estados, y no necesariamente entre los miembros dentro de un mismo estado.'''
st.markdown(f'<div style="text-align: justify">{anova}</div>',unsafe_allow_html=True)


anova2='''Para validar los supuestos de la ANOVA, se llevaron a cabo pruebas de normalidad, homocedasticidad e independencia en los residuales. Los resultados de estas pruebas no respaldan los supuestos necesarios para la ANOVA, lo que indica que los resultados obtenidos podrían ser poco concluyentes.En resumen, aunque la prueba ANOVA mostró diferencias significativas en las medias, la falta de cumplimiento de los supuestos subyacentes sugiere que los resultados deben interpretarse con precaución y podrían no ser definitivos.'''
st.markdown(f'<div style="text-align: justify">{anova2}</div>',unsafe_allow_html=True)
st.image('./images/anova2.png', width=500)
st.image('./images/anova3.png', width=500)
anova3='''
Los resultados de las pruebas de normalidad de Shapiro-Wilk y Kolmogorov-Smirnov indican que los residuos no siguen una distribución normal, ya que ambos p-valores son inferiores al nivel de significancia del 5%. Por lo tanto, con un nivel de confianza del 95%, rechazamos la hipótesis de normalidad de los residuos. Estos hallazgos sugieren que los residuos no se distribuyen de manera normal y que es poco probable que el modelo se ajuste bien a los datos en términos de la suposición de normalidad de los residuos.

El valor del estadístico de Durbin-Watson es de 1.67. Esta medida, que oscila entre 0 y 4, se sitúa en el rango entre 0 y 2. Este resultado sugiere la presencia de cierta autocorrelación positiva en los residuos del modelo. En otras palabras, los residuos adyacentes pueden estar correlacionados positivamente.

La prueba de Levene es una prueba estadística utilizada para evaluar la homogeneidad de las varianzas entre grupos en un análisis de varianza (ANOVA). Su objetivo es determinar si las varianzas de las muestras son iguales o no, lo que es una suposición importante en muchos métodos estadísticos, incluido el ANOVA.

La hipótesis nula de la prueba de Levene es que todas las muestras provienen de poblaciones con la misma varianza. La hipótesis alternativa es que al menos una de las muestras proviene de una población con una varianza diferente. Con un p-valor en la prueba de 0.00107 rechazamos la hipótesis nula, esto es, hay evidencia suficiente de que no se satisface la homocedasticidad
'''
st.markdown(f'<div style="text-align: justify">{anova3}</div>',unsafe_allow_html=True)





st.subheader("Modelos Lineales Generalizados (GLM): Poisson")
glm='''El modelo GLM de Poisson es una extensión del modelo de regresión lineal que se utiliza específicamente para variables de conteo, donde la variable de respuesta representa el número de ocurrencias de un evento en un intervalo fijo de tiempo o espacio. La distribución de Poisson es comúnmente utilizada para modelar este tipo de variables, ya que describe la probabilidad de que ocurran un número dado de eventos en un intervalo fijo, dado un índice medio de ocurrencia.

Al igual que con otros modelos de regresión, la interpretación de los resultados del modelo GLM de Poisson implica examinar los coeficientes de las variables predictoras para determinar su impacto en el número de ocurrencias del evento de interés. Los coeficientes se interpretan como cambios relativos en el logaritmo de la media de la variable de respuesta para un cambio unitario en la variable predictora correspondiente, manteniendo constantes todas las demás variables en el modelo.
'''
st.markdown(f'<div style="text-align: justify">{glm}</div>',unsafe_allow_html=True)
glm1='''
Aunque inicialmente las variables no demostraron ser significativas estadísticamente en el modelo, a través de la exploración de diferentes configuraciones, descubrimos que el modelo final consiste únicamente en la variable de precipitación anual, la cual resulta ser significativa. Este hallazgo resalta la importancia de una exploración minuciosa y adaptable en el proceso de modelado. A pesar de la falta de significancia inicial, la persistencia en probar diferentes configuraciones reveló una relación significativa entre la precipitación anual y la respuesta deseada.
'''
st.markdown(f'<div style="text-align: justify">{glm1}</div>',unsafe_allow_html=True)
glm2='''
Al examinar los modelos ajustados, notamos que la variable de hora (mañana/tarde) no parece tener un efecto significativo en ninguno de los modelos ni en los coeficientes asociados. Sin embargo, al comparar los grupos de NM y AZ, observamos diferencias sustanciales en los modelos ajustados. Estas diferencias se manifiestan tanto en los coeficientes como en la significancia de las componentes. Estos resultados sugieren que, a pesar de la falta de efecto de la hora del día, hay variaciones significativas entre los grupos NM y AZ en términos de las variables predictoras y su impacto en la respuesta. Esta observación resalta la importancia de considerar las diferencias regionales al interpretar los modelos y sus resultados.
'''
st.markdown(f'<div style="text-align: justify">{glm2}</div>',unsafe_allow_html=True)
glm3= '''
Al iterativamente eliminar las variables con los mayores p-valores y ajustar modelos sucesivamente más simples, llegamos a modelos univariados que relacionan el número de alimentos con una sola variable. Al construir un modelo que incluye únicamente la temperatura media, encontramos que esta variable es estadísticamente significativa dentro del modelo. Además, observamos un efecto positivo: a medida que aumenta la temperatura media, aumenta el número de alimentos distintos. Este resultado sugiere una relación significativa y directa entre la temperatura y la diversidad de alimentos en el estudio, lo que resalta la importancia de la temperatura como factor influyente en la variabilidad de la disponibilidad de alimentos.
'''
st.markdown(f'<div style="text-align: justify">{glm3}</div>',unsafe_allow_html=True)


