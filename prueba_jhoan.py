#Esta celda es una prueba

import numpy as np
import matplotlib.pyplot as plt
import random

random.seed(3939)

def poblar(n):
  x = np.zeros(n)
  y = np.zeros(n)
  for i in range (n):
    x[i] = random.randint(0,100)
    y[i] = random.randint(0,100)

  plt.scatter(x, y)
  plt.show()

poblar(00)
