import sys

def solve_case(karel_start, beepers):
    all_points = [karel_start] + beepers
    n = len(all_points)
    
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = abs(all_points[i][0] - all_points[j][0]) + abs(all_points[i][1] - all_points[j][1])
            
    num_states = 1 << n
    dp = [[float('inf')] * n for _ in range(num_states)]
    
    for u in range(n):
        dp[num_states - 1][u] = dist[u][0]
        
    for mask in range(num_states - 2, -1, -1):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            
            for v in range(n):
                if not (mask & (1 << v)):
                    next_mask = mask | (1 << v)
                    cost = dist[u][v] + dp[next_mask][v]
                    if cost < dp[mask][u]:
                        dp[mask][u] = cost
                        
    return dp[1][0]

def read_input():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    num_scenarios = int(input_data[idx])
    idx += 1
    
    for _ in range(num_scenarios):
        idx += 2
        
        karel_x = int(input_data[idx])
        karel_y = int(input_data[idx+1])
        idx += 2
        
        num_beepers = int(input_data[idx])
        idx += 1
        
        beepers = []
        for _ in range(num_beepers):
            bx = int(input_data[idx])
            by = int(input_data[idx+1])
            beepers.append((bx, by))
            idx += 2
            
        ans = solve_case((karel_x, karel_y), beepers)
        print(f"The shortest path has length {ans}")

read_input()