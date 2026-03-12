from sys import stdin

while True:
    n = int(input())
    if n == 0:
        break
    
    c1, n1 = map(int, input().split())
    c2, n2 = map(int, input().split())

    #c es costo x caja y n el maximo de marbles por caja
    
    print(f"{n} {c1} {n1} {c2} {n2}")