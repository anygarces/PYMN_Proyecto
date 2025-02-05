#Super modelo de incendios forestales B)
#JHOAN

import numpy as np
import matplotlib.pyplot as plt
import random

random.seed(3939) #semilla

class Arbol(): #Definimos la clase Arbol
  def __init__(self,id,position,state):
    self.id = id #único a cada arbol para poder identificarlo, en particular el árbol n + 1 que será el origen del incendio
    self.position = position #posición en el plano100 x 100
    self.state = state #SUCEPTIBLE , ENCENDIDO, o MUERTO, que cambiaremos dependiendo de su esta


  def info(self): #método para ver arboles individuales, en particular el primer árbol
    print("el arbol " + str(self.id) + " que está en " + str(self.position) + " actualmente está " +str(self.state))


  def lugar(self): #método devuelve la posición
    return self.position


  def distancia(self, otro_arbol): #método devuelve la distancia entre dos árboles
    d = (((self.position[0] - otro_arbol.position[0])**2) + ((self.position[1] - otro_arbol.position[1])**2))**(1/2)
    print("la distancia entre el árbol " + str(self.id) + " y el árbol " + str(otro_arbol.id) + " es " + str(d))
    return d


  def probabilidad(self,otro_arbol): # de los métodos más importantes que vamos a usar, devuelve la probabilidad de que un árbol ENCENDIDO propague su fuego a otro árbol, y lo vuelva ENCENDIDO

    def distancia(self, otro_arbol): #método devuelve la distancia entre dos árboles
      d = (((self.position[0] - otro_arbol.position[0])**2) + ((self.position[1] - otro_arbol.position[1])**2))**(1/2)
      return d

    p_base = 0.75
    p = p_base / distancia(self, otro_arbol)**2
    print("La probabilidad de transeferencia entre el árbol " + str(self.id) + " y el árbol " + str(otro_arbol.id) + " es de " + str(p))

def crear_arboles(n): #función para crear árboles y posicionarlos

  x = np.zeros(n+2)
  y = np.zeros(n+2)
  lista_arboles = []
  color = ['green']

  for i in range (n): #crea n objetos de la clase Arbol

    x[i] = random.randint(0,100) #posición x aleatoria
    y[i] = random.randint(0,100) #posición y aleatoria

    lista_arboles.append(Arbol(id = i , position = (x[i],y[i]) , state = "SUCEPTIBLE")) #esto añade los arboles a la lista el árbol i
    color.append('green')

  x[n+1] = random.randint(0,100)
  y[n+1] = random.randint(0,100)
  lista_arboles.append(Arbol(id = n + 1 , position = (x[n+1],y[n+1]) , state = "ENCENDIDO")) #esto a+ade a la lista el arbol n + 1, el inicio del incendio
  color.append('red')

  plt.scatter(x,y,c=color) #esto grafica los árboles
  plt.show() #esto también ^^
  return lista_arboles

x = 300

bosque = crear_arboles(x)
bosque[0].info()
bosque[1].info()
bosque[x].info()
bosque[0].distancia(bosque[1])
bosque[0].distancia(bosque[x])
bosque[0].probabilidad(bosque[x])
