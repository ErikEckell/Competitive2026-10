import sys

def precompute_cubrency(max_val):
    coins = [i**3 for i in range(1, 22)]

    dp = [0] * max_val
    dp[0] = 1
    
    for coin in coins:
        for weight in range(coin, max_val):
            dp[weight] += dp[weight - coin]
            
    return dp

def read_input():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    MAX_LIMIT = 10000
    dp_table = precompute_cubrency(MAX_LIMIT)
    
    idx = 0
    while idx < len(input_data):
        amount = int(input_data[idx])
        idx += 1
        print(dp_table[amount])

read_input()