import sys
import heapq

def solve_case(n, m, c, k, input_data, idx):
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    route_cost = [0] * c
    for i in range(c - 2, -1, -1):
        cost_to_next = 0
        for neighbor, weight in adj[i]:
            if neighbor == i + 1:
                cost_to_next = weight
                break
        route_cost[i] = route_cost[i + 1] + cost_to_next
        
    dist = [float('inf')] * n
    pq = []
    
    if k < c:
        return route_cost[k], idx
        
    dist[k] = 0
    heapq.heappush(pq, (0, k))
    
    min_total_cost = float('inf')
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
            
        for v, w in adj[u]:
            if v < c:
                total_cost = d + w + route_cost[v]
                if total_cost < min_total_cost:
                    min_total_cost = total_cost
            else:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
                    
    if dist[c - 1] < min_total_cost:
        min_total_cost = dist[c - 1]
        
    return min_total_cost, idx

def read_input():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        m = int(input_data[idx+1])
        c = int(input_data[idx+2])
        k = int(input_data[idx+3])
        idx += 4
        
        if n == 0 and m == 0 and c == 0 and k == 0:
            break
            
        ans, idx = solve_case(n, m, c, k, input_data, idx)
        print(ans)

read_input()