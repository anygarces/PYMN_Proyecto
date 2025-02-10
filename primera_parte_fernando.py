import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

# -------------------------------
# Configuración inicial
# -------------------------------
random.seed(3939)             # Semilla para reproducibilidad
num_susceptibles = 300        # Número de árboles SUCEPTIBLES
p_base = 0.75                 # Parámetro base para el cálculo de probabilidad
DISTANCIA_MAXIMA = 500        # Distancia máxima para evaluar la propagación

# -------------------------------
# Definición de la clase Arbol
# -------------------------------
class Arbol:
    def __init__(self, id, position, state):
        self.id = id              # Identificador único
        self.position = position  # Posición (x, y)
        self.state = state        # Estado: "SUCEPTIBLE", "ENCENDIDO" o "MUERTO"

    def distancia(self, otro_arbol):
        """Calcula la distancia Euclidiana entre este árbol y otro."""
        d = (((self.position[0] - otro_arbol.position[0])**2) + 
             ((self.position[1] - otro_arbol.position[1])**2))**0.5
        return d

    def probabilidad(self, otro_arbol):
        """
        Calcula la probabilidad de que este árbol (ya ENCENDIDO)
        prenda fuego a otro_arbol.
        Si la distancia es mayor que DISTANCIA_MAXIMA se retorna 0.
        Si la distancia es cero se asigna probabilidad 1 para evitar división por cero.
        En otro caso se utiliza la fórmula:
            p = p_base / (distancia^2)
        Se limita la probabilidad a un máximo de 1.
        """
        d = self.distancia(otro_arbol)
        if d > DISTANCIA_MAXIMA:
            return 0.0
        if d == 0:
            return 1.0
        p = p_base / (d**2)
        return min(1.0, p)

# -------------------------------
# Función para crear el bosque
# -------------------------------
def crear_arboles(n):
    """
    Crea n árboles en estado "SUCEPTIBLE" y un árbol adicional en estado "ENCENDIDO"
    (que actuará como el punto de ignición).  
    Se generan coordenadas aleatorias en el rango [0, 100] para x e y.  
    Retorna la lista de árboles, las coordenadas x, las coordenadas y y la lista inicial de colores.
    """
    x_coords = np.zeros(n+1)
    y_coords = np.zeros(n+1)
    lista_arboles = []
    color_list = []
    
    # Crear los árboles SUCEPTIBLES
    for i in range(n):
        x_coords[i] = random.randint(0, 500)
        y_coords[i] = random.randint(0, 500)
        lista_arboles.append(Arbol(i, (x_coords[i], y_coords[i]), "SUCEPTIBLE"))
        color_list.append("green")
    
    # Crear el árbol ENCENDIDO (el punto de ignición)
    x_coords[n] = random.randint(0, 500)
    y_coords[n] = random.randint(0, 500)
    lista_arboles.append(Arbol(n, (x_coords[n], y_coords[n]), "ENCENDIDO"))
    color_list.append("red")
    
    # (Opcional) Puedes descomentar la siguiente sección para visualizar el estado inicial
    # plt.figure()
    # plt.scatter(x_coords, y_coords, c=color_list)
    # plt.title("Estado inicial del bosque")
    # plt.xlabel("X")
    # plt.ylabel("Y")
    # plt.xlim(0, 100)
    # plt.ylim(0, 100)
    # plt.show()
    
    return lista_arboles, x_coords, y_coords, color_list

# -------------------------------
# Función para actualizar los colores
# -------------------------------
def actualizar_color(bosque):
    """
    Devuelve una lista de colores en función del estado de cada árbol.
      - "SUCEPTIBLE": verde
      - "ENCENDIDO":   rojo
      - "MUERTO":      negro (si se llegara a implementar)
    """
    colores = []
    for arbol in bosque:
        if arbol.state == "SUCEPTIBLE":
            colores.append("green")
        elif arbol.state == "ENCENDIDO":
            colores.append("red")
        elif arbol.state == "MUERTO":
            colores.append("black")
        else:
            colores.append("gray")
    return colores

# -------------------------------
# Función para simular la propagación del incendio
# -------------------------------
def simular_incendio(bosque, max_steps=50):
    """
    Simula la propagación del incendio en pasos discretos.
    En cada paso se evalúa, para cada árbol ENCENDIDO, la posibilidad de prender a los
    árboles SUCEPTIBLES que se encuentren dentro de DISTANCIA_MAXIMA.
    Se guarda una snapshot (lista de colores) del estado del bosque en cada paso.
    """
    snapshots = []
    snapshots.append(actualizar_color(bosque))
    steps = 0
    while steps < max_steps:
        indices_a_actualizar = set()  # Usamos un conjunto para evitar duplicados
        for arbol in bosque:
            if arbol.state == "ENCENDIDO":
                for idx, otro in enumerate(bosque):
                    if otro.state == "SUCEPTIBLE":
                        p = arbol.probabilidad(otro)
                        # Solo se evalúa si p > 0 (están cerca)
                        if p > 0 and p >= random.random():
                            indices_a_actualizar.add(idx)
        # Si en este paso no se enciende ningún árbol, se termina la simulación
        if not indices_a_actualizar:
            break
        # Se actualizan simultáneamente los árboles que pasan a ENCENDIDO
        for idx in indices_a_actualizar:
            bosque[idx].state = "ENCENDIDO"
        steps += 1
        snapshots.append(actualizar_color(bosque))
    return snapshots

# -------------------------------
# Creación y simulación del bosque
# -------------------------------
bosque, x_coords, y_coords, initial_color = crear_arboles(num_susceptibles)
snapshots = simular_incendio(bosque, max_steps=50)

# -------------------------------
# Configuración de la animación
# -------------------------------
fig, ax = plt.subplots()
# Se crea el gráfico de dispersión con las posiciones fijas y los colores de la primera snapshot.
scat = ax.scatter(x_coords, y_coords, c=snapshots[0])
ax.set_xlim(0, 500)
ax.set_ylim(0, 500)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Evolución del incendio en el bosque")

def update(frame):
    """Función que actualiza la gráfica para cada frame (paso) de la animación."""
    colores = snapshots[frame]
    scat.set_color(colores)
    ax.set_title(f"Evolución del incendio - Paso {frame}")
    return scat,

# Aquí se crea la animación.
# Si la animación no funcionara con blit=True, se puede probar cambiándolo a blit=False.
anim = FuncAnimation(fig, update, frames=len(snapshots), interval=500, blit=False, repeat=False)

plt.show()



