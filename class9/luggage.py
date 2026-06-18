import sys

def solve_case(suitcases):
    total_sum = sum(suitcases)
    
    if total_sum % 2 != 0:
        return "NO"
    
    target = total_sum // 2
    
    dp = [False] * (target + 1)
    dp[0] = True
    
    for val in suitcases:
        for w in range(target, val - 1, -1):
            if dp[w - val]:
                dp[w] = True
                
    return "YES" if dp[target] else "NO"

def read_input():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    num_test_cases = int(lines[0])
    
    for i in range(1, num_test_cases + 1):
        if i < len(lines):
            suitcases = list(map(int, lines[i].split()))
            print(solve_case(suitcases))

read_input()