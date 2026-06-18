import sys
import math

def solve_case(coins, S):
    INF = float('inf')
    target = S * S

    dp = [[INF] * (S + 1) for _ in range(S + 1)]
    dp[0][0] = 0

    for conv, info in coins:
        if conv > S or info > S:
            continue
        for x in range(conv, S + 1):
            for y in range(info, S + 1):
                if dp[x - conv][y - info] + 1 < dp[x][y]:
                    dp[x][y] = dp[x - conv][y - info] + 1

    best = INF
    for x in range(S + 1):
        rem = target - x * x
        if rem < 0:
            break
        y = math.isqrt(rem)
        if y * y == rem and y <= S:
            if dp[x][y] < best:
                best = dp[x][y]

    if best == INF:
        return "not possible"
    return best

def read_input():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    num_test_cases = int(input_data[idx])
    idx += 1

    for _ in range(num_test_cases):
        m = int(input_data[idx])
        S = int(input_data[idx+1])
        idx += 2

        coins = []
        for _ in range(m):
            conv = int(input_data[idx])
            info = int(input_data[idx+1])
            coins.append((conv, info))
            idx += 2

        ans = solve_case(coins, S)
        print(ans)

read_input()
