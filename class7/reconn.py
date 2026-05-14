import sys

class disjoint_set:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False

def kruskal(n, edges):
    sorted_edges = sorted(edges, key=lambda x: x[2], reverse=True)
    djs = disjoint_set(n)
    
    mst_cost = 0
    edges_count = 0
    
    while sorted_edges and edges_count < n - 1:
        u, v, w = sorted_edges.pop()
        if not djs.is_same(u, v):
            djs.union(u, v)
            mst_cost += w
            edges_count += 1
            
    return mst_cost

def read_input():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    first_case = True
    
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        
        original_cost = 0
        for _ in range(n - 1):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            w = int(input_data[idx+2])
            original_cost += w
            idx += 3
            
        k = int(input_data[idx])
        idx += 1
        new_plans = []
        for _ in range(k):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            w = int(input_data[idx+2])
            new_plans.append((u, v, w))
            idx += 3
            
        m = int(input_data[idx])
        idx += 1
        all_possible_edges = []
        for _ in range(m):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            w = int(input_data[idx+2])
            all_possible_edges.append((u, v, w))
            idx += 3
            
        all_possible_edges.extend(new_plans)
        
        if not first_case:
            print()
        first_case = False
        
        print(original_cost)
        print(kruskal(n, all_possible_edges))

read_input()