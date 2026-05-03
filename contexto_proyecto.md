# Definición del Proyecto: Análisis de Mortalidad en Guatemala (2013-2022)

Este documento detalla el marco teórico, la problemática y las hipótesis que guían el Análisis Exploratorio de Datos (EDA) y la posterior segmentación (Clustering) de las defunciones en Guatemala.

---

## 1. Situación Problemática

Guatemala atraviesa una transición epidemiológica compleja caracterizada por una **"doble carga de mortalidad"**. 

* Por un lado, persisten problemas de salud pública propios del subdesarrollo, donde la desnutrición crónica afecta al **46.5% de los niños menores de cinco años**, la tasa más alta de América Latina (UNICEF, 2023).
* Por otro lado, la sociedad convive con una epidemia de violencia y siniestralidad vial, registrando tasas de homicidios donde el **88% de las víctimas son hombres**, concentrándose en la población económicamente activa (PNUD, 2024).

Esta polarización se ve agravada por la insuficiencia del sistema de salud pública, cuyo gasto representa apenas el **2.1% del PIB** (OPS, 2023), y por el impacto disruptivo de la pandemia de **COVID-19** en los años 2020 y 2021. 

A pesar de que el Instituto Nacional de Estadística (INE) recopila anualmente los registros de defunciones, la falta de una integración de estos datos en la última década impide visualizar patrones estructurales a largo plazo. Al analizar los años por separado, se invisibilizan los "perfiles de riesgo" reales: no se ha confirmado matemáticamente si la mortalidad en el área rural sigue siendo predominantemente infecciosa/nutricional, en contraste con un área metropolitana dominada por causas externas.

---

## 2. Problema Científico

> Considerando la heterogeneidad social y económica del país, **¿es posible segmentar la mortalidad en Guatemala (2013-2022) en clusters automáticos que validen la existencia de dos perfiles epidemiológicos opuestos: uno determinado por la violencia en la adultez joven y otro por enfermedades prevenibles y naturales en la niñez y vejez, o existen patrones emergentes derivados de la pandemia que rompen esta dicotomía?**

---

## 3. Objetivos

### Objetivo General
Caracterizar los patrones de mortalidad en Guatemala durante la última década mediante técnicas de agrupamiento (Clustering) para identificar perfiles de riesgo que reflejen la polarización entre causas naturales, prevenibles y externas, así como el impacto de crisis sanitarias.

### Objetivos Específicos
1.  **Explorar estadísticamente** la base de datos para validar si la mortalidad masculina presenta un comportamiento anómalo (pico de muertes jóvenes por causas externas) en comparación con la curva de mortalidad femenina.
2.  **Determinar la asociación** entre la ubicación geográfica (Departamento) y las causas de muerte, verificando si existen regiones específicas que concentran sistemáticamente la violencia y los accidentes.
3.  **Generar una segmentación automática (clusters)** que clasifique a la población fallecida en grupos distintivos, permitiendo interpretar la carga de mortalidad asociada a la niñez, la violencia y el impacto del COVID-19.

---

## 4. Preguntas e Hipótesis de Investigación

Las siguientes hipótesis plantean supuestos *a priori* basados en el contexto nacional, los cuales serán validados o refutados mediante el análisis de datos.

### Hipótesis 1: La Brecha de Género y Violencia
* **Supuesto:** Se asume que la esperanza de vida y la curva de mortalidad no son iguales entre sexos. Hipotetizamos que la gráfica de los hombres mostrará un **"pico" anómalo entre los 18 y 35 años** debido a la alta incidencia de homicidios y accidentes, una característica ausente en la curva femenina.

### Hipótesis 2: La Geografía del Peligro
* **Supuesto:** La violencia no se distribuye uniformemente. Creemos que los departamentos de la **Región Metropolitana y Oriente** (Guatemala, Escuintla, Chiquimula) presentan un porcentaje de muertes por "Causas Externas" significativamente mayor que los departamentos del Altiplano Occidental, donde predominan causas naturales.

### Hipótesis 3: Persistencia de la Mortalidad Infantil
* **Supuesto:** A pesar del tiempo, creemos que la mortalidad en el cluster de **0 a 5 años** sigue estando dominada por enfermedades infecciosas (respiratorias/intestinales) y nutricionales, diferenciándose totalmente de las causas de muerte en adultos.

### Hipótesis 4: Concentración de defunciones en fin de semana
* **Supuesto:** Asumimos que la mortalidad por causas externas tiene un componente temporal marcado. Hipotetizamos que los días **sábado y domingo** registran un aumento significativo de defunciones en comparación con los días laborales, impulsado por accidentes de tránsito y hechos delictivos.

### Hipótesis 5: La Anomalía Pandémica (2020-2021)
* **Supuesto:** Asumimos que los años 2020 y 2021 rompen la tendencia estable de la década. Esperamos observar que las **enfermedades respiratorias** desplazan temporalmente a otras causas principales, y que el volumen total de muertes ("Exceso de mortalidad") muestra un pico evidente en estos años.

---

### Referencias Clave
* **UNICEF (2023):** Datos sobre desnutrición crónica infantil.
* **PNUD (2024):** Estadísticas sobre violencia homicida y género.
* **OPS (2023):** Información sobre gasto público en salud.
* **INE (2013-2022):** Bases de datos de Estadísticas Vitales (Fuente primaria).