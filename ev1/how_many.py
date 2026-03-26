import sys

def number_of_divisors(n):
    count = 1
    if n == 1:
        return count
    
    positive_n = abs(n)
    for i in range(2, int(positive_n**0.5) + 1):
        exponent = 0
        while positive_n % i == 0:
            positive_n //= i
            exponent += 1
        count *= (exponent + 1)

    if positive_n > 1:
        count *= 2

    return count

def read_input(infile):
    values = list(map(int, infile.read().split()))
    if not values:
        return
    
    ctr = 0
    while ctr < len(values):
        m = values[ctr]
        n = values[ctr + 1]
        p = values[ctr + 2]

        if (m == n == p == 0):
            break

        num_divs = number_of_divisors(m * n * p * p)
        solutions = ((2 * num_divs) - 1)
        print(f"Case {ctr // 3 + 1}: {solutions}")

        ctr += 3

read_input(sys.stdin)