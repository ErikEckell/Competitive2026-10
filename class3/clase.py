from dataclasses import dataclass

@dataclass #para crear las fucniones dsp igl usa self
class point:
    x: float
    y: float

# class point: #"normal"
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

p = point(1.0, 2.0)
print(p.x, p.y)

@staticmethod
#crea una funcion que no depende de la clase, no necesita self, se puede usar
#sin crear un objeto de la clase, se puede usar con el nombre de la clase
def distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

#definir un punto fuera del poligono y trazar una linea entre este y el punto a verificar
#contar cuantas veces esta linea intersecta con el poligono, si es impar esta dentro, si es par esta fuera

#el convex hull es el poligono convexo mas pequeño que contiene a todos los puntos, 
#se puede usar para encontrar el area de un conjunto de puntos, 
# o para encontrar el perimetro de un conjunto de puntos, 
# o para encontrar el punto mas cercano a un punto dado, 
# o para encontrar el punto mas lejano a un punto dado, 
# o para encontrar el punto mas cercano a una linea dada, 
# o para encontrar el punto mas lejano a una linea dada, 
# o para encontrar el punto mas cercano a un poligono dado, 
# o para encontrar el punto mas lejano a un poligono dado, 
# o para encontrar el punto mas cercano a un conjunto de puntos dado, 
# o para encontrar el punto mas lejano a un conjunto de puntos dado.

#segmentos
#revisar si son colineales: 
#cross product de los vectores pq y pr, si es 0 son colineales

#revisar si se intersectan: