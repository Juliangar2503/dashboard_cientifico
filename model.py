import csv
import json
from collections import defaultdict
from datetime import datetime


class Model:

    def __init__(self):
        self.nombre_archivo_csv = "./data_proyect.csv"
        self.archivo_salida_json = "./data.json"

    # Función para leer datos de un archivo CSV de forma masiva
    def lectura_csv(self):
        data = []
        # Abrir el archivo en modo lectura con with
        with open(self.nombre_archivo_csv, "r", newline='', encoding='utf-8') as file:
            # Crear un objeto DictReader para leer del archivo y devolver cada fila como un dict
            reader = csv.DictReader(file)
            # Leer cada fila del archivo CSV
            for row in reader:
                data.append(row)            
        return data

    def agrupar_datos(self, data):
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

    def cargar_datos_json(self):
        data = self.lectura_csv()
        agrupado = self.agrupar_datos(data)

        with open(self.archivo_salida_json, 'w', encoding='utf-8') as file:
            json.dump(agrupado, file, indent=4, ensure_ascii=False)

    def lectura_json(self):
        with open(self.archivo_salida_json, 'r', encoding='utf-8') as file:
            return json.load(file)
