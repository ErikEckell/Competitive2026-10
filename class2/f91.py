from sys import stdin

def f91(n):
    if n <= 100:
        return f91(f91(n + 11))
    else:
        return n - 10
    
for line in stdin.readlines():
    line = int(line.strip())

    if line == 0:
        break
    
    mcarthy = f91(line)

    print(f"f91({line}) = {mcarthy}")