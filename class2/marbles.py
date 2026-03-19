from sys import stdin
from math import gcd

mem_egcd = {}

def extended_euclid(a, b):
    if (a, b) in mem_egcd:
        return mem_egcd[(a, b)]

    if b == 0:
        ans = (1, 0, a)
        mem_egcd[(a, b)] = ans
        return ans

    x, y, d = extended_euclid(b, a % b)
    ans = (y, x - (a // b) * y, d)
    mem_egcd[(a, b)] = ans
    return ans


def ceil_div(a, b):
    return -((-a) // b)


def marbles(n, c1, n1, c2, n2):
    g = gcd(n1, n2)
    if n % g != 0:
        return None

    x, y, _ = extended_euclid(n1, n2)
    mul = n // g
    x *= mul
    y *= mul

    step_x = n2 // g
    step_y = n1 // g

    k_min = ceil_div(-x, step_x)
    k_max = y // step_y

    if k_min > k_max:
        return None

    slope = c1 * step_x - c2 * step_y
    if slope > 0:
        k = k_min
    elif slope < 0:
        k = k_max
    else:
        k = k_min

    m1 = x + step_x * k
    m2 = y - step_y * k
    return m1, m2


lines = stdin.readlines()
i = 0

while i < len(lines):
    n = int(lines[i].strip())
    i += 1

    if n == 0:
        break

    c1, n1 = map(int, lines[i].split())
    i += 1
    c2, n2 = map(int, lines[i].split())
    i += 1

    ans = marbles(n, c1, n1, c2, n2)
    if ans is None:
        print("failed")
    else:
        print(ans[0], ans[1])