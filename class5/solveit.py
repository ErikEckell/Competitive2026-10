import sys
import math

eps = 1e-9

def f(x, p, q, r, s, t, u):
    return (p * math.exp(-x) + 
            q * math.sin(x) + 
            r * math.cos(x) + 
            s * math.tan(x) + 
            t * x**2 + u)

def solveit(p, q, r, s, t, u):
    f0 = f(0, p, q, r, s, t, u)
    f1 = f(1, p, q, r, s, t, u)

    if f0 * f1 > 0:
        print("No solution")
        return

    low = 0.0
    high = 1.0
    
    while (high - low) > eps:
        mid = (low + high) / 2
        if f(mid, p, q, r, s, t, u) > 0:
            low = mid
        else:
            high = mid
            
    print(f"{high:.4f}")

def read_input(infile):
    values = list(map(int, infile.read().split()))
    if not values:
        return
    
    i = 0
    while i < len(values):
        if i + 5 < len(values):
            p = values[i]
            q = values[i + 1]
            r = values[i + 2]
            s = values[i + 3]
            t = values[i + 4]
            u = values[i + 5]
            solveit(p, q, r, s, t, u)
        i += 6

read_input(sys.stdin)