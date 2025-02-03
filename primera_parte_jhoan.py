#Primera parte
#Super modelo de incendios forestales B)
#JHOAN

import numpy as np
import matplotlib.pyplot as plt
import random

random.seed(3939) #semilla

class Arbol(): #Definimos la clase Arbol
  def __init__(self,id,position,state):
    self.id = id #único a cada arbol para poder identificarlo, en particular el primer árbol que será el origen del incendio
    self.position = position #posición en el plano100 x 100
    self.state = state #Suceptible, encendidio, o muerto, que cambiaremos dependiendo de su esta


  def info(self): #método para ver arboles individuales, en particular el primer árbol
    print("el arbol " + str(self.id) + " que está en " + str(self.position) + " actualmente está " +str(self.state))

def crear_arboles(n): #función para crear árboles y posicionarlos

  x = np.zeros(n)
  y = np.zeros(n)
  lista_arboles = []

  for i in range (n): #crea n objetos de la clase Arbol

    x[i] = random.randint(0,100) #posición x aleatoria
    y[i] = random.randint(0,100) #posición y aleatoria

    lista_arboles.append(Arbol(id = i , position = (x[i],y[i]) , state = "suceptible")) #esto añade los arboles a la lista


  plt.scatter(x,y) #esto grafica los árboles
  plt.show() #esto también ^^
  return lista_arboles

bosque = crear_arboles(100)
bosque[0].info() 
