import sys
import bisect

def solve_case(n, doll_data, idx):
    dolls = []
    for _ in range(n):
        w = int(doll_data[idx])
        h = int(doll_data[idx+1])
        idx += 2
        dolls.append((w, h))
        
    dolls.sort(key=lambda x: (x[0], -x[1]))
    
    lds = []
    
    for _, h in dolls:
        target = -h
        pos = bisect.bisect_right(lds, target)
        if pos < len(lds):
            lds[pos] = target
        else:
            lds.append(target)
            
    return len(lds), idx

def read_input():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    num_test_cases = int(input_data[idx])
    idx += 1
    
    for _ in range(num_test_cases):
        n = int(input_data[idx])
        idx += 1
        
        ans, idx = solve_case(n, input_data, idx)
        print(ans)

read_input()