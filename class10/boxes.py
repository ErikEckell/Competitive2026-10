import sys

def solve_case(n, boxes, idx):
    box_list = []
    for _ in range(n):
        weight = int(boxes[idx])
        max_load = int(boxes[idx+1])
        idx += 2
        box_list.append((weight, max_load))
        
    max_cap = 6002
    dp = [-1] * max_cap
    dp[max_cap - 1] = 0
    
    for weight, max_load in box_list:
        for c in range(max_cap):
            if dp[c] != -1:
                new_cap = min(c - weight, max_load)
                if new_cap >= 0:
                    if dp[c] + 1 > dp[new_cap]:
                        dp[new_cap] = dp[c] + 1
                        
    return max(dp), idx

def read_input():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        
        if n == 0:
            break
            
        ans, idx = solve_case(n, input_data, idx)
        print(ans)

read_input()