#primera parte, Fernando
import numpy as np
import matplotlib.pyplot as plt

# Definición de estados:
# 0: suceptible
# 1: encendido
# 2: muerto

# Creamos un bosque representado como una matriz de 101x101 (o el tamaño que desees)
# Por ejemplo, usaremos un bosque de 101x101 celdas
N = 101
bosque = np.zeros((N, N), dtype=int)

# Inicializamos el árbol que dará inicio al incendio
# Por ejemplo, ponemos el árbol central en estado encendido
centro = N // 2
bosque[centro, centro] = 1

# Visualizamos el bosque usando imshow
plt.imshow(bosque, cmap='viridis', interpolation='none')
plt.colorbar(label="Estado del árbol")
plt.title("Simulación del bosque")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.show()


