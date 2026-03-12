from sys import stdin
import math

def get_divisors(n):
    divisors = []

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    return sorted(divisors)

def min_sum_lcm(n):
    divisors = get_divisors(n)
    min_sum = [2 * n]
    
    def dfs(start, current_lcm, current_sum):
        if current_sum >= min_sum[0] or current_lcm > n:
            return
        
        if current_lcm == n and start > 0:
            min_sum[0] = current_sum
            return
        
        for i in range(start, len(divisors)):
            d = divisors[i]
            new_sum = current_sum + d

            if new_sum >= min_sum[0]:
                break
            
            dfs(i, math.lcm(current_lcm, d), new_sum)
    
    dfs(0, 1, 0)
    return min_sum[0]

case_number = 1
for line in stdin.readlines():
    n = int(line.strip())
    if n == 0:
        break
    print(f"Case {case_number}: {min_sum_lcm(n)}")
    case_number += 1

