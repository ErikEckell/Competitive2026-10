import sys
import math

def build_sk(k):
    parts = []
    for n in range(1, k + 1):
        parts.append("".join(str(i) for i in range(1, n + 1)))
    return "".join(parts)


def solve(x):
    k = math.ceil(((-1 + math.sqrt(1+8*x))/2))
    sk = build_sk(k)
    print(sk[x-1])
    

def read_input(infile):
    values = list(map(int, infile.read().split()))
    if not values:
        return
    
    cases = values[0]
    if cases < 1 or cases > 25:
        return
    
    idx = 1
    while cases > 0:
        solve(values[idx])
        idx += 1
        cases -= 1

read_input(sys.stdin)