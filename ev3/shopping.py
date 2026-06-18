import sys
import math
import functools

def solve_case(n, edges, operas):
    INF = math.inf

    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dist[i][i] = 0
    for a, b, cost in edges:
        if cost < dist[a][b]:
            dist[a][b] = cost
            dist[b][a] = cost
    for k in range(n + 1):
        for i in range(n + 1):
            if dist[i][k] == INF:
                continue
            for j in range(n + 1):
                nd = dist[i][k] + dist[k][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd

    save = {}
    for store, amount in operas:
        save[store] = save.get(store, 0) + amount
    stores = list(save.keys())
    K = len(stores)

    @functools.lru_cache(None)
    def tour(pos, mask):
        if mask == 0:
            return dist[stores[pos]][0]
        best = INF
        m = mask
        while m:
            j = (m & -m).bit_length() - 1
            m &= m - 1
            cost = dist[stores[pos]][stores[j]] + tour(j, mask ^ (1 << j))
            if cost < best:
                best = cost
        return best

    best_net = 0
    for mask in range(1, 1 << K):
        total_save = 0
        m = mask
        while m:
            j = (m & -m).bit_length() - 1
            m &= m - 1
            total_save += save[stores[j]]

        cost = INF
        m = mask
        while m:
            j = (m & -m).bit_length() - 1
            m &= m - 1
            c = dist[0][stores[j]] + tour(j, mask ^ (1 << j))
            if c < cost:
                cost = c

        net = total_save - cost
        if net > best_net:
            best_net = net

    return best_net

def read_input():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    num_scenarios = int(input_data[idx])
    idx += 1

    for _ in range(num_scenarios):
        n = int(input_data[idx])
        m = int(input_data[idx+1])
        idx += 2

        edges = []
        for _ in range(m):
            a = int(input_data[idx])
            b = int(input_data[idx+1])
            cost = round(float(input_data[idx+2]) * 100)
            edges.append((a, b, cost))
            idx += 3

        p = int(input_data[idx])
        idx += 1

        operas = []
        for _ in range(p):
            store = int(input_data[idx])
            amount = round(float(input_data[idx+1]) * 100)
            operas.append((store, amount))
            idx += 2

        best = solve_case(n, edges, operas)
        if best > 0:
            print(f"Daniel can save ${best // 100}.{best % 100:02d}")
        else:
            print("Don't leave the house")

read_input()
