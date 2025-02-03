#primera parte, Fernando
import numpy as np
import matplotlib.pyplot as plt
import random

random.seed(3939)  # semilla

class Arbol():
    def __init__(self, id, position, state):
        self.id = id
        self.position = position
        self.state = state

    def info(self):
        print("El árbol " + str(self.id) + " que está en " + str(self.position) +
              " actualmente está " + str(self.state))

def crear_arboles(n):
    x = np.zeros(n)
    y = np.zeros(n)
    lista_arboles = []
    
    for i in range(n):
        x[i] = random.randint(0, 100)
        y[i] = random.randint(0, 100)
        lista_arboles.append(Arbol(id=i, position=(x[i], y[i]), state="suceptible"))

    # Usamos 's' para que cada punto se vea como un cuadrado
    plt.scatter(x, y, marker='s')
    plt.grid(True)  # Opcional: muestra la cuadricula del gráfico
    plt.show()
    return lista_arboles

bosque = crear_arboles(100)
bosque[0].info()

