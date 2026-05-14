# similar al de mice pero debo considerar reducir el precio por cada conexion intermedia
# cada conexion intermedia de a -> x es un -5% al valor actual, no al original
import sys
from collections import deque

def bfs_distance_to_earth(connections, start_planet):
    if start_planet == 'EARTH':
        return 0
    
    queue = deque([(start_planet, 0)])
    visited = {start_planet}
    
    while queue:
        current, distance = queue.popleft()
        
        for neighbor in connections.get(current, []):
            if neighbor == 'EARTH':
                return distance + 1
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    return float('inf')

def calculate_import_value(planet, planet_values, connections):
    distance = bfs_distance_to_earth(connections, planet)
    if distance == float('inf'):
        return 0
    
    intermediate = distance - 1
    value = planet_values[planet] * (0.95 ** intermediate)
    return value


def read_input(infile):
    lines = infile.readlines()
    if not lines:
        return
    
    idx = 0
    while idx < len(lines):
        while idx < len(lines) and not lines[idx].strip():
            idx += 1
        
        if idx >= len(lines):
            break
        
        planets_amount = int(lines[idx].strip())
        idx += 1
        
        planets = {}
        connections = {}
        
        for _ in range(planets_amount):
            parts = lines[idx].strip().split()
            planet_letter = parts[0]
            planet_value = float(parts[1])
            connections_str = parts[2]
            idx += 1
            
            planets[planet_letter] = planet_value
            connections[planet_letter] = []
            
            for connection_char in connections_str:
                if connection_char == '*':
                    connections[planet_letter].append('EARTH')
                else:
                    connections[planet_letter].append(connection_char)
        
        if planets_amount == 1:
            best_planet = list(planets.keys())[0]
            print(f"Import from {best_planet}")
            continue
        
        values = {}
        for planet in planets:
            values[planet] = calculate_import_value(planet, planets, connections)
        
        best_planet = max(planets.keys(), key=lambda p: (values[p], -ord(p)))
        print(f"Import from {best_planet}")


read_input(sys.stdin)