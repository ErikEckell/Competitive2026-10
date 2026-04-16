import sys
from bisect import bisect_left

def can_fit(capacity, vessels, m):
    """
    Verifica si es posible distribuir la leche en 'm' contenedores
    usando una capacidad máxima 'capacity'.
    """
    if max(vessels) > capacity:
        return False
    
    containers_used = 1
    current_fill = 0
    
    for v in vessels:
        if current_fill + v > capacity:
            containers_used += 1
            current_fill = v
        else:
            current_fill += v
            
    return containers_used <= m

class CapacityWrapper:
    """
    Objeto virtual para que bisect_left busque la capacidad mínima.
    """
    def __init__(self, vessels, m, low, high):
        self.vessels = vessels
        self.m = m
        self.low = low
        self.high = high

    def __len__(self):
        # El tamaño del rango de búsqueda
        return self.high - self.low + 1

    def __getitem__(self, capacity_offset):
        # Mapeamos el índice de la búsqueda al valor real de capacidad
        actual_capacity = self.low + capacity_offset
        
        # Queremos encontrar el primer valor que sea FACTIBLE.
        # bisect_left busca el primer valor 'True'. 
        # Python trata True como 1 y False como 0.
        return can_fit(actual_capacity, self.vessels, self.m)

def solveit(n, m, vessels):
    # El rango de búsqueda para la capacidad mínima:
    # Mínimo: el recipiente más grande (porque no se puede partir la leche de un vaso).
    # Máximo: la suma de todos los recipientes (un solo contenedor).
    low = max(vessels)
    high = sum(vessels)
    
    wrapper = CapacityWrapper(vessels, m, low, high)
    
    # Buscamos el primer valor de capacidad (1) que cumpla can_fit
    idx = bisect_left(wrapper, True)
    
    print(low + idx)

def read_input(infile):
    # Mantenemos tu estructura de lectura exacta
    input_data = infile.read().split()
    if not input_data:
        return
    
    values = list(map(int, input_data))
    
    i = 0
    while i < len(values):
        n = values[i]
        m = values[i + 1]
        # Los siguientes 'n' valores son las capacidades de los vasos
        vessels = values[i + 2 : i + 2 + n]
        
        solveit(n, m, vessels)
        
        # Saltamos n (vasos) + 2 (n y m)
        i += (n + 2)

read_input(sys.stdin)