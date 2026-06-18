import sys

def solve_case(n, k):
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            min_cost = float('inf')

            for m in range(i, j + 1):
                current_cost = dp[i][m-1] + dp[m+1][j] + (j - i + 1) * (k + m)
                if current_cost < min_cost:
                    min_cost = current_cost
                    
            dp[i][j] = min_cost
            
    return dp[1][n]

def read_input():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    num_test_cases = int(input_data[idx])
    idx += 1
    
    for case_num in range(1, num_test_cases + 1):
        n = int(input_data[idx])
        k = int(input_data[idx+1])
        idx += 2
        
        ans = solve_case(n, k)
        print(f"Case {case_num}: {ans}")

read_input()