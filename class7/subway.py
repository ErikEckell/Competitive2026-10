import sys
import math
import heapq

def read_case(tokens):
    hx, hy = int(next(tokens)), int(next(tokens))
    sx, sy = int(next(tokens)), int(next(tokens))
    nodes = [(hx, hy), (sx, sy)]
    subway_edges = []
    while True:
        try:
            tx = int(next(tokens))
            ty = int(next(tokens))
        except StopIteration:
            break
        if tx == -1 and ty == -1:
            continue
        line = [(tx, ty)]
        while True:
            nx = int(next(tokens))
            ny = int(next(tokens))
            if nx == -1 and ny == -1:
                break
            line.append((nx, ny))
        idxs = []
        for stop in line:
            if stop in nodes:
                idxs.append(nodes.index(stop))
            else:
                nodes.append(stop)
                idxs.append(len(nodes)-1)
        for i in range(len(idxs)-1):
            a, b = idxs[i], idxs[i+1]
            d = math.hypot(nodes[a][0] - nodes[b][0], nodes[a][1] - nodes[b][1])
            subway_edges.append((a, b, d))
    return nodes, subway_edges

def read_input():
    lines = sys.stdin.read().splitlines()
    tokens = (token for line in lines for token in line.strip().split())
    try:
        T = int(next(tokens))
    except StopIteration:
        return
    for case_idx in range(T):
        # Saltar líneas vacías
        while True:
            try:
                peek = next(tokens)
                tokens = (t for t in [peek] + list(tokens))
                break
            except StopIteration:
                return
        nodes, subway_edges = read_case(tokens)
        n = len(nodes)
        v_walk = 10000 / 60.0
        v_subway = 40000 / 60.0
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                d = math.hypot(nodes[i][0] - nodes[j][0], nodes[i][1] - nodes[j][1])
                t = d / v_walk
                adj[i].append((j, t))
                adj[j].append((i, t))
        for u, v, d in subway_edges:
            t = d / v_subway
            adj[u].append((v, t))
            adj[v].append((u, t))
        dist = [float('inf')] * n
        dist[0] = 0.0
        heap = [(0.0, 0)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))
        print(int(dist[1]+0.5))
        if case_idx < T-1:
            print()

read_input()