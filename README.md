# Análisis de Mortalidad en Guatemala (2013-2022)

##  Introducción

Este proyecto realiza un análisis exploratorio y de segmentación (clustering) de los patrones de mortalidad en Guatemala durante la década 2013-2022. El objetivo es identificar perfiles de riesgo que reflejen la polarización entre causas naturales, prevenibles y externas, así como el impacto de crisis sanitarias como la pandemia de COVID-19.

---

##  Estructura del Proyecto

```
proyecto1/
│
├── README.md                          # Este archivo
├── contexto_proyecto.md               # Definición del proyecto, problemática e hipótesis
├── diccionario.md                     # Descripción completa de variables y mapeos
│
├── main.ipynb                         # Notebook principal con análisis EDA y clustering
│
├── data/
│   └── variables/                 # Archivos de referencia para mapeo de variables
│   │   └── definicion.xlsx        # Mapeo CIE-10 para descripción de causas
│   ├── defunciones/                   # Datos brutos del INE (2013-2022)
│   │   ├── 2013.sav
│   │   ├── 2014.sav
│   │   ├── 2015.sav
│   │   ├── 2016.sav
│   │   ├── 2017.sav
│   │   ├── 2018.sav
│   │   ├── 2019.sav
│   │   ├── 2020.sav
│   │   ├── 2021.sav
│   │   └── 2022.sav
│
└── src/                               # Scripts y funciones auxiliares (si los hay)
```

