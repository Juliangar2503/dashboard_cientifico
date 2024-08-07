from model import Model
# ********************************************************
import json
import matplotlib.pyplot as plt
from datetime import datetime

class Controller:
    def __init__(self) -> None:
        self.model = Model()
        self.data = self.model.lectura_json()

    def plot(self, graphic_name):
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
        plt.title('Defunciones por Día de la Semana')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()