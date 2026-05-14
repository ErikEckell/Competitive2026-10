import sys
import heapq

def dijkstra(routes, from_planet, to_planet):
    dist = {from_planet: 0}
    parent = {from_planet: None}
    steps = {from_planet: 1}

    next_vertex = [from_planet]
    while len(next_vertex):
        u = next_vertex.pop()
        
        if u == to_planet:
            continue

        for (v, w) in routes.get(u, []):
            new_dist = dist[u] + w
            new_steps = steps[u] + 1
            
            if v not in dist or (new_dist < dist[v]) or (new_dist == dist[v] and new_steps < steps[v]):
                dist[v] = new_dist
                parent[v] = u
                steps[v] = new_steps
                if v not in next_vertex:
                    next_vertex.append(v)
        
        next_vertex.sort(key=lambda x: -dist[x])

    path = []
    curr = to_planet
    while curr is not None:
        path.append(curr)
        curr = parent.get(curr)
    
    return " ".join(path[::-1])


def read_input():
    lines = sys.stdin.readlines()
    if not lines:
        return
    
    idx = 0
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    if idx >= len(lines):
        return
    
    planets_amount = int(lines[idx][0].strip())
    routes_amount = int(lines[idx][2].strip())

    # print(f"Planets: {planets_amount}, Routes: {routes_amount}")

    routes = {}

    for line in lines[idx+1:idx+1+routes_amount]:
        # print(f"Line: {line.strip()}")
        if line.strip():
            parts = line.strip().split()
            if len(parts) == 3:
                planet_a, planet_b, distance = parts
                distance = int(distance)
                if planet_a not in routes:
                    routes[planet_a] = []
                if planet_b not in routes:
                    routes[planet_b] = []
                routes[planet_a].append((planet_b, distance))
                routes[planet_b].append((planet_a, distance))

    queries = []

    for line in lines[idx+1+routes_amount:]:
        # print(f"Line: {line.strip()}")
        if line.strip():
            parts = line.strip().split()
            if len(parts) == 2:
                planet_a, planet_b = parts
                queries.append((planet_a, planet_b))

    # print(f"Routes: {routes}")
    # print(f"Queries: {queries}")

    for query in queries:
        result = dijkstra(routes, query[0], query[1])
        print(result)

read_input()