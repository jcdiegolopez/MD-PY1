# Diccionario de Datos: Defunciones INE (Guatemala)

Este documento describe las variables contenidas en los archivos `.sav` (SPSS) del Instituto Nacional de Estadística (INE) consolidados para el periodo 2013-2022.

##  Tabla de Variables

| Acrónimo (Variable en .sav) | Nombre Completo | Tipo de Variable | Significado | Notas de Disponibilidad / Uso |
| :--- | :--- | :--- | :--- | :--- |
| **Depreg** | Departamento de registro | Cualitativa nominal | Departamento donde se registró la defunción |  Disponible en todos los años |
| **Mupreg** | Municipio de registro | Cualitativa nominal | Municipio donde se registró la defunción |  Disponible en todos los años |
| **Mesreg** | Mes de registro | Cualitativa ordinal | Mes en que se realizó el registro |  Disponible en todos los años |
| **Añoreg** | Año de registro | Cuantitativa discreta | Año en que se registró la defunción |  Disponible en todos los años |
| **Depocu** | Departamento de ocurrencia | Cualitativa nominal | Departamento donde ocurrió la defunción |  Disponible en todos los años. **Usar esta para análisis geográfico.** |
| **Mupocu** | Municipio de ocurrencia | Cualitativa nominal | Municipio donde ocurrió la defunción |  Disponible en todos los años |
| **Diaocu** | Día de ocurrencia | Cuantitativa discreta | Día del mes en que ocurrió la defunción |  Disponible en todos los años |
| **Mesocu** | Mes de ocurrencia | Cualitativa ordinal | Mes en que ocurrió la defunción |  Disponible en todos los años |
| **Añoocu** | Año de ocurrencia | Cuantitativa discreta | Año en que ocurrió la defunción |  **Disponible consistentemente solo de 2015 en adelante.** Para años anteriores, validar con `Añoreg`. |
| **Areag** | Área geográfica | Cualitativa nominal | Clasificación: Urbana o Rural |  Disponible en todos los años |
| **Ocur** | Sitio de ocurrencia | Cualitativa nominal | Lugar físico (Hospital, Casa, Vía Pública) |  Disponible en todos los años |
| **Sexo** | Sexo del difunto(a) | Cualitativa nominal | Sexo biológico (1=Hombre, 2=Mujer) |  Disponible en todos los años |
| **Edadif** | Edad del difunto(a) | Cuantitativa discreta | Edad en años cumplidos |  Disponible en todos los años. (Requiere limpieza de códigos 999). |
| **Perdif** | Período de edad | Cualitativa ordinal | Clasificación por rangos de edad |  Disponible en todos los años |
| **Puedif** | Pueblo de pertenencia | Cualitativa nominal | Grupo étnico (Maya, Ladino, etc.) |  Disponible en todos los años |
| **Ecidif** | Estado civil | Cualitativa nominal | Estado civil al momento de la defunción |  Disponible en todos los años |
| **Escodif** | Escolaridad | Cualitativa ordinal | Nivel educativo alcanzado |  Disponible en todos los años |
| **Ciuodif** | Ocupación (CIUO-08) | Cualitativa nominal | Ocupación según clasificación internacional |  Disponible en todos los años |
| **Pnadif** | País de nacimiento | Cualitativa nominal | País donde nació el difunto(a) |  Disponible en todos los años |
| **Dnadif** | Depto. de nacimiento | Cualitativa nominal | Departamento donde nació el difunto(a) |  Disponible en todos los años |
| **Mnadif** | Municipio de nacimiento | Cualitativa nominal | Municipio donde nació el difunto(a) |  Disponible en todos los años |
| **Nacdif** | Nacionalidad | Cualitativa nominal | Nacionalidad registrada |  Disponible en todos los años |
| **Predif** | País de residencia | Cualitativa nominal | País donde residía el difunto(a) |  Disponible en todos los años |
| **Dredif** | Depto. de residencia | Cualitativa nominal | Departamento de residencia habitual |  Disponible en todos los años |
| **Mredif** | Municipio de residencia | Cualitativa nominal | Municipio de residencia habitual |  Disponible en todos los años |
| **Caudef** | Causa de defunción | Cualitativa nominal | Código CIE-10 de la causa base |  **REQUIERE MAPEO EXTERNO** (Ver sección inferior). |
| **caudef.descrip** | Descripción de causa | Cualitativa nominal | Descripción textual |  **NO UTILIZAR.** No disponible consistentemente en los datasets. Usar mapeo de `Caudef`. |
| **Asist** | Asistencia recibida | Cualitativa nominal | Tipo de asistencia médica recibida |  Disponible en todos los años |
| **Cerdef** | Quién certifica | Cualitativa nominal | Persona/Institución que certifica |  Disponible en todos los años |

---

##  Mapeo de Causas de Muerte (CIE-10)

La columna principal para el análisis de causas es **`Caudef`**. Esta columna contiene códigos alfanuméricos (Ej: `X99`, `I21`) que corresponden a la Clasificación Internacional de Enfermedades (CIE-10).

Para obtener la descripción textual de estos códigos, **se debe realizar un JOIN o Merge** con el archivo maestro de variables ubicado en este repositorio.

###  Ubicación del archivo de mapeo
* **Path:** `data/variables/definicion.xlsx`
* **Hoja (Sheet):** `CIE-10`

### Estructura del Excel para el Join:
* **Columna 1:** Código CIE-10 (Llave primaria para cruzar con `Caudef`) a partir de la tercara fila (A3).
* **Columna 2:** Descripción de la enfermedad/causa a partir de la tercera fila (B3).

### Códigos de causas de muerte utilizados de la Clasificación Internacional de Enfermedades CIE-10
| Descripción | CIE9 | CIE10 |
|---|---|---|
| Todas las causas de muerte | Todos los códigos | Todos los códigos |
| Enfermedades infecciosas | 001-139 + 279.1 + 279.8 | A00-A99 + B00-B99 |
| Septicemia | O38 | A40-A41 |
| SIDA | 279.5-279.6 | B20-B24 |
| Tumores malignos | 140-208 | C00-C97 |
| Tumor maligno de estómago | 151 | C16 |
| Tumor maligno de colon y recto | 153-154 | C18-C20 |
| Tumor maligno tráquea/bronquios/pulmón | 162 | C33-C34 |
| Tumor maligno de mama | 174 | C50 |
| Tumor maligno de próstata | 185 | C61 |
| Enfermedades endocrinas/metabólicas/inmunidad | 240-279 (menos 279.5+279.6) | E00-E90, D80-D89 |
| Diabetes mellitus | 250 | E10-E14 |
| Trastornos mentales | 290-319 | F00-F99 |
| Sistema nervioso y órganos sentidos | 320-389 | G00-G98, H00-H65 |
| Alzheimer | 331.0 | G30 |
| Aparato circulatorio | 390-459 | I00-I99 |
| Enfermedad hipertensiva | 401-405 | I10-I13 |
| Enfermedades del corazón | 390-398,402,404-429 | I00-I09,I11,I13,I20-I51 |
| Enfermedad isquémica corazón | 410-414 | I20-I25 |
| Enfermedad cerebrovascular | 430-438 | I60-I69 |
| Aparato respiratorio | 460-519 | J00-J99 |
| Neumonía e influenza | 480-487 | J10-J18 |
| EPOC | 490-496 | J40-J47 |
| Aparato digestivo | 520-579 | K00-K93 |
| Enfermedad crónica hígado | 571 | K70 + K73-K74 |
| Apendicitis | 540-543 | K35-K38 |
| Hernia abdominal | 550-553 + 560 | K40-K46 + K56 |
| Aparato genitourinario | 580-629 | N00-N99 |
| Nefritis / síndrome nefrótico | 580-589 | N00-N07, N17-N19, N25-N27 |
| Accidentes y causas externas | 800-999 | V00-V99 + W00-W99 + X00-X99 + Y00-Y99 |
| Accidentes no intencionales | 800-949 | V01-X59,Y85-Y86 |
| Accidentes de tráfico | 810-819 | (lista extensa V02-V89 según documento) |
| Suicidio | 950-959 | X60-X84 + Y87.0 |
| Homicidio | 960-969 | X85-X99 + Y00-Y09 + Y87.1 |
| Efectos adversos medicamentos | 930-949 | Y40-Y59 |
---

##  Consideraciones de Limpieza Temporal

1.  **Año de Ocurrencia (`Añoocu`):** Esta variable presenta inconsistencias o ausencia de datos en los archivos anteriores a **2015**.
    * *Estrategia:* Para análisis de series temporales completos (2013-2022), se recomienda validar contra `Añoreg` o imputar con cuidado en años previos a 2015.
2.  **Caudef.descrip:** Esta variable debe ser **inutilizada** del dataframe consolidado durante la fase de pre-procesamiento para evitar ruido, ya que está vacía en la mayoría de los años.
3.  **Edadif (codigo 999):** El valor 999 indica edad no declarada y debe ser tratado como dato faltante antes de calcular estadisticas o distribuciones.
4.  **Areag (Área geográfica):** Esta variable presenta **alto porcentaje de datos faltantes** y no se recomienda para análisis exploratorio. Usar en su lugar **`Depreg`** (Departamento de registro) o **`Depocu`** (Departamento de ocurrencia) para análisis geográficos.