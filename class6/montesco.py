import sys
from collections import deque

def solve_case(n, adj):
    color = [0] * (n + 1) 
    max_invite = 0

    for i in range(1, n + 1):
        if color[i] == 0:
            q = deque([i])
            color[i] = 1
            count = [0, 0, 0]  
            count[1] = 1
            bipartite = True
            
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        count[color[v]] += 1
                        q.append(v)
                    elif color[v] == color[u]:
                        bipartite = False
            
            if bipartite:
                max_invite += max(count[1], count[2])
            else:
                pass
                
    print(max_invite)

def read_input(infile):
    lines = [line.rstrip('\n') for line in infile]
    idx = 0
    
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    
    if idx >= len(lines):
        return
        
    try:
        t_cases = int(lines[idx].strip())
        idx += 1
    except ValueError:
        return

    for _ in range(t_cases):
        while idx < len(lines) and not lines[idx].strip():
            idx += 1
        
        if idx >= len(lines):
            break
            
        try:
            n = int(lines[idx].strip())
            idx += 1
        except ValueError:
            break
            
        adj = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            while idx < len(lines) and not lines[idx].strip():
                idx += 1
                
            if idx < len(lines):
                parts = list(map(int, lines[idx].strip().split()))
                for enemy in parts[1:]:
                    if 1 <= enemy <= n:
                        adj[i].append(enemy)
                        adj[enemy].append(i)
                idx += 1
        
        solve_case(n, adj)

read_input(sys.stdin)