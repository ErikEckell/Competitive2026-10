import sys

def solve_case(variables, constraints):
    vars_sorted = sorted(variables)
    adj = {v: [] for v in vars_sorted}
    indegree = {v: 0 for v in vars_sorted}
    
    for c in constraints:
        u, v = c[0], c[2]
        adj[u].append(v)
        indegree[v] += 1

    results = []

    def find_all_topological_orders(current_order, current_indegree):
        if len(current_order) == len(vars_sorted):
            results.append(" ".join(current_order))
            return

        found_candidate = False
        for v in vars_sorted:
            if v not in current_order and current_indegree[v] == 0:
                found_candidate = True
                
                for neighbor in adj[v]:
                    current_indegree[neighbor] -= 1
                
                current_order.append(v)
                
                find_all_topological_orders(current_order, current_indegree)
                
                current_order.pop()
                for neighbor in adj[v]:
                    current_indegree[neighbor] += 1

    find_all_topological_orders([], indegree)

    if not results:
        print("NO")
    else:
        for res in results:
            print(res)

def read_input():
    lines = sys.stdin.readlines()
    if not lines:
        return
    
    idx = 0
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    if idx >= len(lines):
        return
        
    num_test_cases = int(lines[idx].strip())
    idx += 1
    
    for t in range(num_test_cases):
        while idx < len(lines) and not lines[idx].strip():
            idx += 1
        
        if idx < len(lines):
            variables = lines[idx].strip().split()
            idx += 1
            
            while idx < len(lines) and not lines[idx].strip():
                idx += 1
            constraints = lines[idx].strip().split()
            idx += 1
            
            solve_case(variables, constraints)
            
            if t < num_test_cases - 1:
                print()

if __name__ == "__main__":
    read_input()