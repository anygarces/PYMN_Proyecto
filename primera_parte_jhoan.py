#Super modelo de incendios forestales B)
#JHOAN

import numpy as np
import matplotlib.pyplot as plt
import random

random.seed(3939) #semilla

x = 1000
p_base = 0.2

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

  def averiguar_probabilidad(self,otro_arbol):
    def distancia(self, otro_arbol): #método devuelve la distancia entre dos árboles
      d = (((self.position[0] - otro_arbol.position[0])**2) + ((self.position[1] - otro_arbol.position[1])**2))**(1/2)
      return d

    p = p_base / distancia(self, otro_arbol)**2
    print("La probabilidad de transeferencia entre el árbol " + str(self.id) + " y el árbol " + str(otro_arbol.id) + " es de " + str(p))
    return p


  def probabilidad(self,otro_arbol): # de los métodos más importantes que vamos a usar, devuelve la probabilidad de que un árbol ENCENDIDO propague su fuego a otro árbol, y lo vuelva ENCENDIDO

    def distancia(self, otro_arbol): #método devuelve la distancia entre dos árboles
      d = (((self.position[0] - otro_arbol.position[0])**2) + ((self.position[1] - otro_arbol.position[1])**2))**(1/2)
      return d

    p = p_base / distancia(self, otro_arbol)**3
    return p


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


def iniciar_incendio():
  copia_bosque = bosque
  color = []
  x = []
  y = []

  muertos = 0
  encendidos = 0

  for k in range (len(bosque)):
    if bosque[k].state == 'SUCEPTIBLE':
      color.append('green')
    elif bosque[k].state == 'ENCENDIDO':
      color.append('red')
    elif bosque[k].state == 'MUERTO':
      color.append('black')

  for l in range (len(bosque)):
    x.append(bosque[l].position[0])
    y.append(bosque[l].position[1])

  for i in range (len(bosque)):

    if bosque[i].state == 'ENCENDIDO':
     for j in range (len(bosque)):
      if bosque[j].state == 'SUCEPTIBLE':
        if bosque[i].probabilidad(bosque[j]) >= random.random():
          copia_bosque[j].state = 'ENCENDIDO'

        else:
          True
      else:
        True
    else:
      True

  plt.scatter(x,y,c=color)
  plt.show()

  for r in range (len(bosque)):
    if bosque[r].state == 'ENCENDIDO':
      encendidos = encendidos + 1
    
    elif bosque[r].state == 'MUERTO':
      muertos = muertos + 1


  if muertos == len(bosque) or encendidos == len(bosque):
    return

  iniciar_incendio()
  

bosque = crear_arboles(x)
bosque[0].info()
bosque[1].info()
bosque[x].info()
bosque[0].distancia(bosque[1])
bosque[0].distancia(bosque[x])
bosque[0].averiguar_probabilidad(bosque[x])

iniciar_incendio()
