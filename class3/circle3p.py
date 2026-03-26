from sys import stdin
import math

def solve_system(A, b):
    n = len(A)

    for i in range(n):
        A[i].append(b[i])
    
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        
        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i]
            for j in range(i, n + 1):
                A[k][j] -= factor * A[i][j]
    
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    
    return x

def solve_circle(x1, y1, x2, y2, x3, y3):
    A = [
        [x1, y1, 1],
        [x2, y2, 1],
        [x3, y3, 1]
    ]
    b = [
        -(x1**2 + y1**2),
        -(x2**2 + y2**2),
        -(x3**2 + y3**2)
    ]
    
    D, E, F = solve_system(A, b)
    return D, E, F

for line in stdin.readlines():
    line = line.strip()
    
    if not line:
        break
    
    numeros = list(map(float, line.split()))
    ax, ay, bx, by, cx, cy = numeros

    D, E, F = solve_circle(ax, ay, bx, by, cx, cy)

    h = -D / 2
    k = -E / 2
    r = math.sqrt(h**2 + k**2 - F)
    
    eps = 1e-9

    def fmt_paren(val, var):
        """(x - h)^2 o x^2"""
        return f"({var} {'-' if val >= 0 else '+'} {abs(val):.3f})^2" if abs(val) > eps else f"{var}^2"
    
    def fmt_term(val, var=""):
        """Terminal + Dx o + D"""
        if abs(val) < eps:
            return ""
        sign = "+" if val >= 0 else "-"
        return f" {sign} {abs(val):.3f}{var}"

    x_part = fmt_paren(h, "x")
    y_part = fmt_paren(k, "y")
    r_str = f"{r:.3f}^2" if abs(r) > eps else "0"
    eq2 = f"x^2 + y^2{fmt_term(D, 'x')}{fmt_term(E, 'y')}{fmt_term(F)}"

    print(f"{x_part} + {y_part} = {r_str}")
    print(f"{eq2} = 0")
    print()