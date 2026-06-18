import sys

def is_inside(n, vertices, px, py):
    inside = False
    
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        
        if x1 == x2:
            if min(y1, y2) <= py < max(y1, y2):
                if x1 > px:
                    inside = not inside
                    
    return "T" if inside else "F"

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
            
        vertices = []
        for _ in range(n):
            vx = int(input_data[idx])
            vy = int(input_data[idx+1])
            vertices.append((vx, vy))
            idx += 2
            
        px = int(input_data[idx])
        py = int(input_data[idx+1])
        idx += 2
        
        print(is_inside(n, vertices, px, py))

read_input()