from controller import Controller 
class Menu:
     
    def __init__(self) -> None:
        self.controller = Controller()

    def run(self):
        while(True):
            print("""Seleccione la grafica a visualizar:
            1) Defunciones diarias
            2) Casos diarias
            3) Hospitalizados diarias
            4) UCI diarias
            5) Diagrama de defunciones por ciudad
            6) Diagrama de Casos por ciudad
            7) Diagrama de Hospitalizados por ciudad
            8) Diagrama de UCI por ciudad
            9) Salir
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
                self.controller.create_cake('num_def')
            elif opt == '6':
                self.controller.create_cake('new_cases')
            elif opt == '7':
                self.controller.create_cake('num_hosp')
            elif opt == '8':
                self.controller.create_cake('num_uci')
            elif opt == '9':
                print("Saliendo...")
                break


            else:
                print("Opción no disponible")
     