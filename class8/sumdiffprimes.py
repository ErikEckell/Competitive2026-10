import sys

def get_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def precompute_dp(max_n, max_k):
    primes = get_primes(max_n)
    
    dp = [[0] * (max_k + 1) for _ in range(max_n + 1)]
    dp[0][0] = 1
    
    for p in primes:
        for w in range(max_n, p - 1, -1):
            for c in range(max_k, 0, -1):
                dp[w][c] += dp[w - p][c - 1]
                
    return dp

def read_input():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    MAX_N = 1120
    MAX_K = 14
    dp_table = precompute_dp(MAX_N, MAX_K)
    
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        k = int(input_data[idx+1])
        idx += 2
        
        if n == 0 and k == 0:
            break
            
        print(dp_table[n][k])

read_input()