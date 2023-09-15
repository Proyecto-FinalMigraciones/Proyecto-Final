
## ANÁLISIS DE FLUJOS MIGRATORIOS

### Data Science - Proyecto Final

![PF]()

#

En este proyecto, nuestro equipo de **BAMK Data Solution** se ha propuesto analizar y comprender en profundidad los **`flujos migratorios internacionales`** y los factores que los impulsan. La migración humana es un fenómeno global que ha sido una constante a lo largo de la historia y que sigue siendo relevante en la actualidad. Este análisis proporcionará información valiosa para comprender cómo la migración afecta a diferentes aspectos socioeconómicos y geopolíticos en todo el mundo.


## Contexto

Los flujos migratorios se han incrementado a lo largo de los años debido a una variedad de factores, que incluyen problemas socioeconómicos, conflictos bélicos, desempleo y falta de acceso a la educación. En este proyecto, nos centraremos en identificar los principales países de origen de los migrantes y sus países de destino, así como en comprender las razones fundamentales que llevan a las personas a tomar la decisión de migrar.


## Objetivos

Nuestros objetivos son:

- Analizar y comprender los **`Flujos Migratorios`**.
- Recopilar y consolidar datos históricos.
- Identificar países de *origen y destino* mas relevantes.
- Reconocer los *principales factores* que motivan la migración, considerando aspectos socioeconómicos, políticos y medioambientales.
- Crear una solución de datos integral que incluya un pipeline de datos, una base de datos, un data warehouse, modelos predictivos y un dashboard para visualizar los resultados.
- Generar un informe detallado que presente los hallazgos clave y las relaciones entre los flujos migratorios y los factores principales de migración.
- Evaluar el impacto de los flujos migratorios en los países de origen y destino en términos de cambios demográficos, economía y cultura.


## Alcance

En este proyecto, nos enfocaremos en el análisis de flujos migratorios internacionales y los factores motivadores que los impulsan. El alcance de nuestro análisis abarcará los años comprendidos entre 2000 y 2020. Nos centraremos en los 10 países de origen y destino más frecuentes en este período. Además, exploraremos en profundidad las razones detrás de estos movimientos.

## Datasets

De donde fueron extraidos y cuales son

## Stack Tecnológico

![Diagrama]()

## Data Engineering

Que pasos se realizaron

## Data Analytics

### EDA 

Se realizó un **`análisis exploratorio`** de datos de flujos migratorios, donde se exploraron diversos aspectos fundamentales relacionados con los movimientos poblacionales en diferentes países y rutas migratorias. El propósito principal ha sido obtener una comprensión profunda de las tendencias generales, los patrones y los factores determinantes que influyen en los desplazamientos de personas en el contexto actual.

A lo largo del análisis, se han destacado varios hallazgos:

- **Tendencias Globales:** Se ha constatado un aumento constante en los flujos migratorios a lo largo de los años, lo que sugiere un fenómeno de alcance global y en constante evolución.

- **Regiones de Origen y Destino:** Se han identificado regiones y países que actúan como puntos de origen y destino para los migrantes. Estos patrones obedecen a una variedad de factores, entre ellos los económicos y sociales, que impulsan los movimientos poblacionales.

- **Factores Económicos:** Se ha observado una relación entre el crecimiento del Producto Interno Bruto (PIB) de un país y la cantidad de inmigrantes que buscan establecerse en él. Los países con economías más robustas tienden a atraer a individuos en busca de empleo y oportunidades financieras.

- **Refugiados y Conflictos:** Se ha evidenciado que una porción de los flujos migratorios ocurre en regiones afectadas por conflictos armados y situaciones de crisis.

- **Distribución de Género:** Se ha analizado la distribución de género en los flujos migratorios y se ha observado que las migraciones a menudo involucran tanto a hombres como a mujeres en proporciones similares.


En resumen, el análisis de los datos resalta la naturaleza de los flujos migratorios y cómo su dinámica es moldeada por una diversidad de factores interrelacionados.

Estos son los EDA reaizados a cada dataset:

[Origen y Destino](https://github.com/Proyecto-FinalMigraciones/Proyecto-Final/blob/main/EDA/migracion_origen_destino_EDA.ipynb)

[Factores/Indicadores migratorios](https://github.com/Proyecto-FinalMigraciones/Proyecto-Final/blob/main/EDA/indicadores_EDA.ipynb)

[Mujeres migrantes](https://github.com/Proyecto-FinalMigraciones/Proyecto-Final/blob/main/EDA/migrantes_mujeres_EDA.ipynb)

Refugiados [País de asilo](https://github.com/Proyecto-FinalMigraciones/Proyecto-Final/blob/main/EDA/refugiados_pais_asilo_EDA.ipynb) y
[País de origen](https://github.com/Proyecto-FinalMigraciones/Proyecto-Final/blob/main/EDA/refugiados_pais_origen_EDA.ipynb)


## Machine Learning

Se planteó como objetivo de Machine Learning desarrollar un modelo basado en *regresión lineal* para predecir flujos migratorios utilizando las columnas 'Crecimiento_PIB', 'Tasa_desempleo', 'Muertes_Conflicto' y 'Control_Corrupción' como características de entrenamiento y 'Migración_neta' como la variable objetivo.

Este modelo se implementó en una interfaz web utilizando **FastAPI** y se desplegó en la plataforma [Render](https://prediccion-migracion.onrender.com/docs#/), a través de la cual los usuarios pueden acceder a tres endpoints:

1. **Predicción por País**: El usuario selecciona un país y recibe una predicción específica de flujos migratorios para ese país.

2. **Predicción para Todos los Países**: Sin necesidad de ingresar un país específico, el sistema genera automáticamente una lista de predicciones de flujos migratorios para todos los países en los datos.

3. **Predicción Personalizada**: Permite al usuario ingresar valores personalizados para las características, y el sistema calcula y muestra una predicción manual de flujos migratorios basada en los valores proporcionados.

Posteriormente, se implementó **`Streamlit`** para mejorar la interfaz y ofrecer una experiencia de usuario aún más intuitiva y amigable.

[Deploy](https://app-es5fro8b28h3zqzp264cuk.streamlit.app/)

## Dashboard

### Portada

Página principal que ofrece una visión general de los flujos migratorios y acceso a otras secciones del dashboard.

![Portada]()

### Página 1 - Factores Migratorios

![Factores migratorios]()

Muestra gráficos de factores clave relacionados con la migración, como el crecimiento del PIB, el control de la corrupción, la tasa de desempleo, la migración neta y la población total de cada país.

### Página 2 - Origen y Destino / Refugiados

![Origen y Destino]()

Compara la población desglosada por género, en países de origen y destino, y ofrece información sobre la cantidad de personas que buscan refugio en comparación con las que abandonan sus países de origen.

### Página 3 - KPIs de Países de Origen

![KPI's Países Origen]()

Presenta los **`Indicadores Clave de Desempeño (KPIs)`** de los países de **origen** más frecuentes de emigración.
- Reducción de la tasa de desempleo en un 3% en los próximos 2 años.
- Reducción de la tasa de migración neta en un 1% en el próximo año.

### Página 4 - KPIs de Países Destino

![KPI's Países Destino]()

En sintonía con la página anterior, esta sección presenta los Indicadores Clave de Desempeño (KPIs) de los países de **Destino** más habituales para la inmigración
- Reducir la tasa de desempleo en un 3% en los próximos 2 años .
- Reducir la tasa de migración neta en un 1% en el próximo año. 

### Página 5 - Modelo

![KPI's Países Destino]()

Dedicada al análisis del modelo de predicción que proporciona conclusiones relevantes relacionadas con los flujos migratorios. Se basa en datos extraídos de la API creada para el proyecto.

## Conclusiones

## Authors

- [Brenda]()
- [Angie](https://github.com/Angiea18)
- [Miller](https://github.com/Milalex19)
- [Kevin](https://github.com/KevinBonnin)

![Logo BAMK]()
