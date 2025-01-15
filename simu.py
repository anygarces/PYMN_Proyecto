#simulacion de los planetas

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

# Cargar los datos del archivo CSV (reemplazar con el nombre de tu archivo)
data = pd.read_csv('orbitas.txt')
#data.columns = data.columns.str.strip() 


# Crear una figura y ejes
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-8e11, 8e11)  # Ajustar límites según el rango de posiciones
ax.set_ylim(-8e11, 8e11)
ax.set_aspect('equal')
ax.set_title("Movimiento de los planetas alrededor del Sol")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")

# Agregar el Sol en el centro
ax.plot(0, 0, 'yo', label="Sol", markersize=10)

# Lista de planetas (nombres a partir del archivo)
planetas = ['mercurio', 'venus', 'tierra', 'marte', 'jupiter']
colores = ['gray', 'orange', 'blue', 'red', 'brown']  # Colores para cada planeta

# Diccionario para almacenar los puntos de los planetas
planet_markers = {}

# Inicializar los puntos en la gráfica
for planeta, color in zip(planetas, colores):
    planet_markers[planeta], = ax.plot([], [], 'o', label=planeta.capitalize(), color=color)

# Función de inicialización
def init():
    for planeta in planetas:
        planet_markers[planeta].set_data([], [])
    return planet_markers.values()

# Función de actualización para cada frame
def update(frame):
    current_data = data[data['t'] == frame]
    for planeta in planetas:
        x_col = f'x_{planeta}'
        y_col = f'y_{planeta}'
        if x_col in data.columns and y_col in data.columns:
            x = current_data[x_col].values[0]
            y = current_data[y_col].values[0]
            planet_markers[planeta].set_data(x, y)
    return planet_markers.values()

# Crear la animación
frames = data['t'].unique()  # Lista de tiempos únicos
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)

# Agregar una leyenda
ax.legend(loc="upper left")

# Mostrar la animación
plt.show()

