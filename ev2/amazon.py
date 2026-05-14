import sys
from collections import deque

def solve(stations):
    n = len(stations)
    if n == 1:
        print("All stations are reachable.")
        return
    
    graph = [[] for _ in range(n)]

    for i in range(n):
        distances = []
        for j in range(n):
            if i != j:
                x1, y1 = stations[i]
                x2, y2 = stations[j]
                dist = (x1 - x2)**2 + (y1 - y2)**2

                distances.append((dist, stations[j][0], -stations[j][1], j))
        #print(distances)
        
        distances.sort()
        
        #print(distances)
        for k in range(min(2, len(distances))):
            graph[i].append(distances[k][3])
    #print(graph)
    
    visited = set([0])
    queue = deque([0])
    
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if u not in visited:
                visited.add(u)
                queue.append(u)
    
    if len(visited) == n:
        print("All stations are reachable.")
    else:
        print("There are stations that are unreachable.")

def read_input(infile):
    values = list(map(int, infile.read().split()))
    if not values:
        return
    
    idx = 0
    n = values[idx]
    idx += 1
    
    while n != 0:
        stations = []
        for i in range(n):
            x = values[idx]
            y = values[idx + 1]
            stations.append((x, y))
            idx += 2

        #print(stations)
        
        solve(stations)
        
        n = values[idx]
        idx += 1

read_input(sys.stdin)