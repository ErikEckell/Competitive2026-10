import sys

def solve_case(case_num, n, to):
    memo = [0] * (n + 1)

    def dfs(u):
        if memo[u]:
            return memo[u]
        memo[u] = 1
        memo[u] += dfs(to[u]) if memo[to[u]] == 0 else memo[to[u]]
        return memo[u]

    # Detect cycles and avoid infinite recursion
    visited = [0] * (n + 1)
    def dfs_cycle(u):
        stack = []
        curr = u
        while True:
            if memo[curr]:
                break
            if visited[curr]:
                # Found a cycle
                cycle_start = stack.index(curr)
                cycle_len = len(stack) - cycle_start
                for i in range(cycle_start, len(stack)):
                    memo[stack[i]] = cycle_len
                break
            visited[curr] = 1
            stack.append(curr)
            curr = to[curr]
        for i in range(len(stack)-1, -1, -1):
            if not memo[stack[i]]:
                memo[stack[i]] = memo[to[stack[i]]] + 1

    for i in range(1, n+1):
        if not memo[i]:
            visited = [0] * (n + 1)
            dfs_cycle(i)

    max_reach = -1
    answer = 1
    for i in range(1, n+1):
        if memo[i] > max_reach or (memo[i] == max_reach and i < answer):
            max_reach = memo[i]
            answer = i
    print(f"Case {case_num}: {answer}")


def read_input(infile):
    values = list(map(int, infile.read().split()))
    if not values:
        return
    idx = 0
    T = values[idx]; idx += 1
    for case_num in range(1, T+1):
        n = values[idx]; idx += 1
        to = [0] * (n + 1)
        for _ in range(n):
            u = values[idx]; idx += 1
            v = values[idx]; idx += 1
            to[u] = v
        solve_case(case_num, n, to)

read_input(sys.stdin)