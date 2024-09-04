#Punto 8
from Paquete1.Trabajo_practico_7_puntos_1_al_7 import Restaurante

class Sandwicheria(Restaurante):
    def __init__(self, restaurante_nombre, tipo_comida, sabores):
        super().__init__(restaurante_nombre, tipo_comida)
        self.sabores = sabores

    def mostrar_sabores(self):
        print(f"Opciones disponibles en {self.restaurante_nombre}:")
        for sabor in self.sabores:
            print(f"- {sabor}")
            
Sandwicheria1 = Sandwicheria("Comilona", "Sandwicheria", ["Mila", "Hamburguesa", "Lomo", "Pancho"])

Sandwicheria1.describir_restaurante()

Sandwicheria1.abrir_restaurante()

Sandwicheria1.mostrar_sabores()