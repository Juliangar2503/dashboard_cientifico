from model import Model
import matplotlib.pyplot as plt
from datetime import datetime

class Controller:
    def __init__(self) -> None:
        self.model = Model()
        self.data = self.model.lectura_json()

    def plot_metric(self, graphic_name):
        dias = []
        valores = []
        for dia, provincias in self.data.items():
            for provincia, indicadores in provincias.items():
                dias.append(dia)
                if graphic_name == "Defunciones":
                    valores.append(indicadores['num_def'])
                elif graphic_name == "Casos":
                    valores.append(indicadores['new_cases'])
                elif graphic_name == "Hospitalizados":
                    valores.append(indicadores['num_hosp'])
                elif graphic_name == "UCI":
                    valores.append(indicadores['num_uci'])
                else:
                    print(f"Gráfico no reconocido: {graphic_name}")
                    return
        
        plt.figure(figsize=(10, 5))
        plt.bar(dias, valores, color='red')
        plt.xlabel('Día de la Semana')
        plt.ylabel(f'Número {graphic_name}')
        plt.title(f'{graphic_name} por Día de la Semana')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def group_by_province(self):
        ciudades = {}
        for dia, provincias in self.data.items(): 
            for provincia, indicadores in provincias.items():
                if provincia not in ciudades:
                    ciudades[provincia] = {
                        'num_def': 0,
                        'new_cases': 0,
                        'num_hosp': 0,
                        'num_uci': 0
                    }

                ciudades[provincia]['num_def'] += indicadores.get('num_def', 0)
                ciudades[provincia]['new_cases'] += indicadores.get('new_cases', 0)
                ciudades[provincia]['num_hosp'] += indicadores.get('num_hosp', 0)
                ciudades[provincia]['num_uci'] += indicadores.get('num_uci', 0)
        return ciudades

    def search_max(self, tipo):
        ciudades = self.group_by_province()
        max_num_def = {
            'provincia' : '',
            'num_max' : 0
        }
        max_new_cases= {
            'provincia' : '',
            'num_max' : 0
        }
        max_num_hosp = {
            'provincia' : '',
            'num_max' : 0
        }
        max_num_uci = {
            'provincia' : '',
            'num_max' : 0
        }
       
        for provincia, indicadores_totales in ciudades.items():
            if ( indicadores_totales['num_def'] > max_num_def['num_max']):
                max_num_def['num_max'] = max(max_num_def['num_max'], indicadores_totales['num_def'])
                max_num_def['provincia'] = provincia
            if ( indicadores_totales['new_cases'] > max_new_cases['num_max']):
                max_new_cases['num_max'] = max(max_new_cases['num_max'], indicadores_totales['new_cases'])
                max_new_cases['provincia'] = provincia
            if ( indicadores_totales['num_hosp'] > max_num_hosp['num_max']):
                max_num_hosp['num_max'] = max(max_num_hosp['num_max'], indicadores_totales['num_hosp'])
                max_num_hosp['provincia'] = provincia
            if ( indicadores_totales['num_uci'] > max_num_uci['num_max']):
                max_num_uci['num_max'] = max(max_num_uci['num_max'], indicadores_totales['num_uci'])
                max_num_uci['provincia'] = provincia
                     
        if(tipo == 'num_def'):
            print("Provincia con mínimo de defunciones:", max_num_def)
        if(tipo == 'new_cases'):
            print("Provincia con mínimo de nuevos casos:", max_new_cases)
        if(tipo == 'num_hosp'):
            print("Provincia con mínimo de hospitalizados:", max_num_hosp)
        if(tipo == 'num_uci'):
            print("Provincia con mínimo de UCI:", max_num_uci)
        
    def search_min(self, tipo):
        ciudades = self.group_by_province()
        min_num_def = {
            'provincia': '',
            'num_min': float('inf')  # Iniciar con infinito positivo
        }
        min_new_cases = {
            'provincia': '',
            'num_min': float('inf')
        }
        min_num_hosp = {
            'provincia': '',
            'num_min': float('inf')
        }
        min_num_uci = {
            'provincia': '',
            'num_min': float('inf')
        }
       
        for provincia, indicadores_totales in ciudades.items():
            if ( indicadores_totales['num_def'] < min_num_def['num_min']):
                min_num_def['num_min'] = min(min_num_def['num_min'], indicadores_totales['num_def'])
                min_num_def['provincia'] = provincia
            if ( indicadores_totales['new_cases'] < min_new_cases['num_min']):
                min_new_cases['num_min'] = min(min_new_cases['num_min'], indicadores_totales['new_cases'])
                min_new_cases['provincia'] = provincia
            if ( indicadores_totales['num_hosp'] < min_num_hosp['num_min']):
                min_num_hosp['num_min'] = min(min_num_hosp['num_min'], indicadores_totales['num_hosp'])
                min_num_hosp['provincia'] = provincia
            if ( indicadores_totales['num_uci'] < min_num_uci['num_min']):
                min_num_uci['num_min'] = min(min_num_uci['num_min'], indicadores_totales['num_uci'])
                min_num_uci['provincia'] = provincia
                     
        if(tipo == 'num_def'):
            print("Provincia con mínimo de defunciones:", min_num_def)
        if(tipo == 'new_cases'):
            print("Provincia con mínimo de nuevos casos:", min_new_cases)
        if(tipo == 'num_hosp'):
            print("Provincia con mínimo de hospitalizados:", min_num_hosp)
        if(tipo == 'num_uci'):
            print("Provincia con mínimo de UCI:", min_num_uci)
        
    def create_cake(self, tipo):
        provincias = []
        valores = []
        global_data = self.group_by_province()
        for provincia, indicadores in global_data.items():
            provincias.append(provincia)
            valores.append(indicadores[tipo])
        
        plt.figure(figsize=(8, 6))
        plt.pie(valores, labels=provincias, autopct='%1.1f%%', startangle=140)
        plt.title(f'Grafica de {tipo}')
        plt.axis('equal')  # Para que el gráfico sea un círculo perfecto
        plt.show()

        self.search_max(tipo)
        self.search_min(tipo)

        