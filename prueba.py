import csv
import json
from collections import defaultdict
from datetime import datetime

# Función para leer datos de un archivo CSV de forma masiva
def leer_de_fichero(nombre_archivo):
    data = []
    # Abrir el archivo en modo lectura con with
    with open(nombre_archivo, "r", newline='', encoding='utf-8') as file:
        # Crear un objeto DictReader para leer del archivo y devolver cada fila como un dict
        reader = csv.DictReader(file)
        # Leer cada fila del archivo CSV
        for row in reader:
            data.append(row)            
    return data

def agrupar_datos(data):
    agrupado = defaultdict(lambda:defaultdict(lambda:{
        'num_def': 0,
        'new_cases': 0,
        'num_hosp': 0,
        'num_uci': 0
    }))

    for row in data:
        fecha = row.get('date')
        provincia = row.get('province')
        num_def = int(row.get('num_def', 0))
        new_cases = int(row.get('new_cases', 0))
        num_hosp = int(row.get('num_hosp', 0))
        num_uci = int(row.get('num_uci', 0))

       # Comprobar si fecha es válida
        if not fecha:
            continue
        
        try:
            fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')
            dia_semana = fecha_dt.strftime('%A')
        except ValueError:
            # Si la fecha está mal formateada, continuar con la siguiente fila
            continue

        # Acumulación de los datos
        agrupado[dia_semana][provincia]['num_def'] += num_def
        agrupado[dia_semana][provincia]['new_cases'] += new_cases
        agrupado[dia_semana][provincia]['num_hosp'] += num_hosp
        agrupado[dia_semana][provincia]['num_uci'] += num_uci

    return agrupado

def guardar_en_json(agrupado, archivo_salida):
     with open(archivo_salida, 'w', encoding='utf-8') as file:
        json.dump(agrupado, file, indent=4, ensure_ascii=False)

path = "./data_proyect.csv"
json_path = "./data.json"
data = leer_de_fichero(path)
agrupado = agrupar_datos(data)
guardar_en_json(agrupado, json_path)