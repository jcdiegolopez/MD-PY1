import openpyxl
from openpyxl.utils import get_column_letter
import json
import os
from pathlib import Path

def detectar_tipo_encabezado(ws):
    """
    Detecta si una tabla tiene encabezados simples (1 fila) o agrupados (2 filas).
    
    Lógica:
    - AGRUPADA: Fila 9 tiene sub-encabezados donde fila 8 está vacío (estructura multi-nivel)
    - SIMPLE: Fila 8 tiene encabezados, fila 9 tiene DATOS (números, texto de datos)
    
    Retorna: 'simple' o 'agrupado'
    """
    # Contar patrones
    fila8_con_valor = 0
    fila9_con_valor = 0
    fila9_donde_fila8_vacio = 0  # Columnas donde 8 es vacío pero 9 tiene valor (sub-encabezados)
    fila9_donde_fila8_lleno = 0   # Columnas donde ambas tienen valor
    
    for col in range(1, 100):
        col_letter = get_column_letter(col)
        valor8 = ws[f'{col_letter}8'].value
        valor9 = ws[f'{col_letter}9'].value
        
        if valor8:
            fila8_con_valor += 1
        
        if valor9:
            fila9_con_valor += 1
            
            if not valor8:
                # Fila 9 tiene valor pero fila 8 no -> es sub-encabezado
                fila9_donde_fila8_vacio += 1
            else:
                # Ambas filas tienen valor -> probablemente es dato
                fila9_donde_fila8_lleno += 1
        
        # Parar si llegamos a muchas columnas vacías
        if col > 50 and fila8_con_valor == 0 and fila9_con_valor == 0:
            break
    
    # Decisión mejorada:
    # Si hay SUB-encabezados (fila9_donde_fila8_vacio > 0), es agrupado
    # BUT: Si la mayoría de fila9 contiene valores donde fila8 TAMBIÉN tiene valores,
    #      probablemente sea datos simples (no sub-encabezados)
    
    if fila9_donde_fila8_vacio > 0 and fila9_donde_fila8_vacio >= fila9_donde_fila8_lleno:
        # Hay sub-encabezados y son más o igual que datos
        return 'agrupado'
    else:
        # Fila 9 probablemente tiene datos, no sub-encabezados
        return 'simple'

def leer_encabezados_simple(ws, max_col=50):
    """
    Lee encabezados de una tabla simple (una sola fila).
    Los encabezados están SOLO en fila 8.
    Fila 9 contiene datos, no sub-encabezados.
    """
    encabezados = []
    
    col = 1
    while col <= max_col:
        col_letter = get_column_letter(col)
        valor = ws[f'{col_letter}8'].value
        
        if not valor:
            break
        
        nombre_col = str(valor).strip()
        encabezados.append(nombre_col)
        col += 1
    
    return encabezados

def leer_encabezados_agrupado(ws, max_col=50):
    """
    Lee encabezados de una tabla agrupada (dos filas).
    Los encabezados principales están en fila 8, los sub-encabezados en fila 9.
    Detecta celdas combinadas.
    
    Retorna una estructura armada con título principal y subtítulos:
    - Si tiene subtítulos reales: {"titulo_principal": ["subtitulo1", "subtitulo2"]}
    - Si NO tiene subtítulos: {"titulo_principal": "solo_nombre"}
    """
    estructura = {}
    grupos_con_subtitulos = {}  # Para rastrear si un grupo tiene subtítulos reales
    
    # Mapear celdas combinadas
    mapa_combinadas = {}
    for rango_combinado in ws.merged_cells.ranges:
        min_col = rango_combinado.min_col
        max_col_rango = rango_combinado.max_col
        min_row = rango_combinado.min_row
        max_row = rango_combinado.max_row
        
        # Si es una celda combinada horizontal en fila 8
        if min_row == 8 and max_row == 8 and min_col < max_col_rango:
            col_letter = get_column_letter(min_col)
            valor = ws[f'{col_letter}8'].value
            
            for col in range(min_col, max_col_rango + 1):
                mapa_combinadas[col] = valor
    
    # Leer encabezados
    col = 1
    while col <= max_col:
        col_letter = get_column_letter(col)
        
        valor_principal = ws[f'{col_letter}8'].value
        valor_secundario = ws[f'{col_letter}9'].value
        
        # Aplicar mapeo de combinadas
        if col in mapa_combinadas:
            valor_principal = mapa_combinadas[col]
        
        # Si no hay valores, terminar
        if not valor_principal and not valor_secundario:
            break
        
        # Procesar según el valor principal
        if valor_principal:
            valor_principal = str(valor_principal).strip()
            
            # Inicializar grupo si no existe
            if valor_principal not in estructura:
                estructura[valor_principal] = []
                grupos_con_subtitulos[valor_principal] = False
        
        # Agregar subtítulo si existe
        if valor_secundario:
            valor_secundario = str(valor_secundario).strip()
            if valor_principal:
                estructura[valor_principal].append(valor_secundario)
                grupos_con_subtitulos[valor_principal] = True
            else:
                # No debería ocurrir en agrupadas, pero por seguridad
                if "sin_grupo" not in estructura:
                    estructura["sin_grupo"] = []
                    grupos_con_subtitulos["sin_grupo"] = True
                estructura["sin_grupo"].append(valor_secundario)
        
        col += 1
    
    # Convertir a strings aquellos grupos sin subtítulos reales
    resultado = {}
    for titulo, valores in estructura.items():
        if grupos_con_subtitulos.get(titulo, False) and valores:
            # Tiene subtítulos reales, mantener como lista
            resultado[titulo] = valores
        else:
            # No tiene subtítulos reales, convertir a string
            resultado[titulo] = titulo
    
    return resultado

def extraer_estructura_tabla(archivo_excel, nombre_hoja):
    """
    Extrae solo la estructura (encabezados) de una tabla.
    Detecta automáticamente si es simple o agrupada.
    
    Retorna para SIMPLE: 
        {'tipo': 'simple', 'encabezados': [...], 'total_columnas': int}
    
    Retorna para AGRUPADO:
        {'tipo': 'agrupado', 'encabezados': {titulo: [subtitulos] o titulo: "nombre"}, 'total_columnas': int}
    """
    try:
        wb = openpyxl.load_workbook(archivo_excel, data_only=True)
        ws = wb[nombre_hoja]
        
        # Detectar tipo de encabezado
        tipo = detectar_tipo_encabezado(ws)
        
        # Leer encabezados según tipo
        if tipo == 'agrupado':
            encabezados = leer_encabezados_agrupado(ws)
            # Contar total de columnas (suma de subtítulos + strings individuales)
            total_cols = 0
            for valor in encabezados.values():
                if isinstance(valor, list):
                    total_cols += len(valor)
                else:  # Es un string sin subtítulos
                    total_cols += 1
        else:
            encabezados = leer_encabezados_simple(ws)
            total_cols = len(encabezados)
        
        wb.close()
        
        return {
            'tipo': tipo,
            'encabezados': encabezados,
            'total_columnas': total_cols
        }
    
    except Exception as e:
        print(f"  Error: {e}")
        return {'tipo': 'error', 'encabezados': {}, 'error': str(e), 'total_columnas': 0}

def main():
    # Configuración
    directorio_data = 'data/defunciones'
    mapeo_json = 'data/json/mapeo_hojas.json'
    estructura_json = 'data/json/estructura_completa.json'
    años_procesamiento = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
    
    print("=" * 70)
    print("EXTRAYENDO ESTRUCTURA DE COLUMNAS - TODOS LOS AÑOS (2015-2024)")
    print("=" * 70)
    
    # Verificar si existe mapeo_hojas.json
    if not os.path.exists(mapeo_json):
        print(f"\n❌ Error: {mapeo_json} no existe. Ejecuta primero el script de mapeo.")
        return
    
    # Cargar mapeo
    print(f"\n✓ Leyendo {mapeo_json}...")
    with open(mapeo_json, 'r', encoding='utf-8') as f:
        mapeo = json.load(f)
    
    # Estructura resultado: {tema: {año: estructura}}
    estructura_resultado = {}
    resumen_años = {}
    
    # Por cada año
    for año in años_procesamiento:
        print(f"\n{'='*70}")
        print(f"PROCESANDO AÑO {año}")
        print(f"{'='*70}")
        
        archivo_año = os.path.join(directorio_data, f'{año}.xlsx')
        
        if not os.path.exists(archivo_año):
            print(f"\n⚠ {archivo_año} no existe, saltando...")
            resumen_años[año] = {'procesadas': 0, 'error': 'Archivo no existe'}
            continue
        
        print(f"✓ Procesando {año}.xlsx...")
        
        temáticas_procesadas = 0
        agrupadas_año = 0
        simples_año = 0
        total_cols_año = 0
        
        # Por cada temática
        for tematica, años_map in mapeo.items():
            nombre_hoja = años_map.get(año)
            
            if not nombre_hoja:
                continue
            
            # Inicializar entrada para temática si no existe
            if tematica not in estructura_resultado:
                estructura_resultado[tematica] = {}
            
            # Extraer estructura
            estructura = extraer_estructura_tabla(archivo_año, nombre_hoja)
            
            estructura['hoja'] = nombre_hoja
            estructura_resultado[tematica][año] = estructura
            
            temáticas_procesadas += 1
            total_cols_año += estructura['total_columnas']
            
            if estructura['tipo'] == 'agrupado':
                agrupadas_año += 1
            else:
                simples_año += 1
            
            print(f"  [{temáticas_procesadas}] {tematica[:50]}... ({estructura['tipo']}, {estructura['total_columnas']} cols)")
        
        resumen_años[año] = {
            'procesadas': temáticas_procesadas,
            'agrupadas': agrupadas_año,
            'simples': simples_año,
            'total_columnas': total_cols_año
        }
    
    # Guardar resultado
    print("\n" + "=" * 70)
    print("GUARDANDO RESULTADO")
    print("=" * 70)
    
    with open(estructura_json, 'w', encoding='utf-8') as f:
        json.dump(estructura_resultado, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Estructura guardada en: {estructura_json}")
    
    # Resumen general
    print("\n" + "=" * 70)
    print("RESUMEN GENERAL")
    print("=" * 70)
    
    print(f"\nAños procesados: {len(años_procesamiento)}")
    for año in años_procesamiento:
        if año in resumen_años:
            info = resumen_años[año]
            if 'error' in info:
                print(f"  {año}: ⚠ {info['error']}")
            else:
                print(f"  {año}: {info['procesadas']} temáticas ({info['agrupadas']} agrupadas, {info['simples']} simples, {info['total_columnas']} cols)")
    
    total_temáticas = len(estructura_resultado)
    total_años_completos = sum(1 for y in años_procesamiento if y in resumen_años and 'error' not in resumen_años[y])
    
    print(f"\nTotal temáticas: {total_temáticas}")
    print(f"Años completos: {total_años_completos}/{len(años_procesamiento)}")
    
    print("\n" + "=" * 70)
    print("PROCESO COMPLETADO")
    print("=" * 70)

def leer_estructura_columnas(archivo_excel, nombre_hoja):
    """
    Esta función está deprecada. Usar extraer_estructura_tabla() en su lugar.
    """
    pass

if __name__ == "__main__":
    main()
