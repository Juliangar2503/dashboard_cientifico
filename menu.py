from controller import Controller 
class Menu:
     
    def __init__(self) -> None:
        self.controller = Controller()

    def run(self):
        while(True):
            print("""Seleccione la grafica a visualizar:
            1) Defunciones
            2) Casos
            3) Hospitalizados
            4) UCI
            5) Salir
            """)
            opt = input("Introduce una opcion: ")
            if opt == '1':
                graphic_name = "Defunciones"
                self.controller.plot_metric(graphic_name)         
            elif opt == '2':
                graphic_name = "Casos"
                self.controller.plot_metric(graphic_name)  
            elif opt == '3':
                graphic_name = "Hospitalizados"
                self.controller.plot_metric(graphic_name)  
            elif opt == '4':
                graphic_name = "UCI"
                self.controller.plot_metric(graphic_name)  
            elif opt == '5':
                print("Saliendo...")
                break
            elif opt == '6':
                print(self.controller.search_max())
            elif opt == '7':
                print(self.controller.search_min())
            elif opt == '8':
                self.controller.crear_pastel(['Provincia A', 'Provincia B', 'Provincia C'], [120, 150, 80], 'Defunciones por Provincia')


            else:
                print("Opción no disponible")
     