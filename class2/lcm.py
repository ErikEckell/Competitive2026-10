from sys import stdin

def min_sum_lcm(n):
    if n == 1:
        return 2

    x = n
    total = 0
    terms = 0
    p = 2

    while p * p <= x:
        if x % p == 0:
            prime_power = 1

            while x % p == 0:
                x //= p
                prime_power *= p

            total += prime_power
            terms += 1

        p += 1 if p == 2 else 2

    if x > 1:
        total += x
        terms += 1

    if terms == 1:
        return total + 1
    return total

case_number = 1

for line in stdin.readlines():
    n = int(line.strip())

    if n == 0:
        break
    
    print(f"Case {case_number}: {min_sum_lcm(n)}")
    case_number += 1

