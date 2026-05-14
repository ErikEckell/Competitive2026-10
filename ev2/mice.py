import sys
from bisect import bisect_left

def dijkstra(connections, from_cell, exit_cell):
    import heapq
    heap = [(0, from_cell)]
    visited = set()
    
    while heap:
        time, cell = heapq.heappop(heap)
        if cell in visited:
            continue
        visited.add(cell)
        
        if cell == exit_cell:
            return time
        
        for neighbor, t in connections.get(cell, []):
            if neighbor not in visited:
                heapq.heappush(heap, (time + t, neighbor))
    
    return float('inf')  # No se puede llegar a la salida

def read_input(infile):
    values = list(map(int, infile.read().split()))
    if not values:
        return

    idx = 0
    cases_amt = values[idx]
    idx += 1
    for _ in range(cases_amt):
        if idx >= len(values):
            break

        connections = {}
        cells_amount = values[idx]
        idx += 1
        exit_cell = values[idx]
        idx += 1
        timer = values[idx] 
        idx += 1
        connections_amt = values[idx]
        idx += 1
        
        for _ in range(connections_amt):
            first_cell, second_cell, time = values[idx:idx+3]
            if first_cell not in connections:
                connections[first_cell] = []
            connections[first_cell].append((second_cell, time))
            idx += 3

        mice = 0
        for cell_num in range(1, cells_amount + 1):
            min_time = dijkstra(connections, cell_num, exit_cell)
            if min_time <= timer:
                mice += 1
        
        print(mice)
        print()
        #print(idx, cells_amount, exit_cell, timer, connections_amt)


read_input(sys.stdin)