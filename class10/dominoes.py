import sys

def backtrack(space_count, last_number, n, m, pieces, used, right_target):
    if space_count == n:
        return last_number == right_target
        
    for i in range(m):
        if not used[i]:
            u, v = pieces[i]
            
            if u == last_number:
                used[i] = True
                if backtrack(space_count + 1, v, n, m, pieces, used, right_target):
                    return True
                used[i] = False
                
            if v == last_number:
                used[i] = True
                if backtrack(space_count + 1, u, n, m, pieces, used, right_target):
                    return True
                used[i] = False
                
    return False

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
            
        m = int(input_data[idx])
        idx += 1
        
        left_u = int(input_data[idx])
        left_v = int(input_data[idx+1])
        idx += 2
        
        right_u = int(input_data[idx])
        right_v = int(input_data[idx+1])
        idx += 2
        
        pieces = []
        for _ in range(m):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            pieces.append((u, v))
            idx += 2
            
        used = [False] * m
        if backtrack(0, left_v, n, m, pieces, used, right_u):
            print("YES")
        else:
            print("NO")

read_input()