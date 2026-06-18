import sys

def solve_case(objects, people):
    max_weight_needed = max(people)
    
    dp = [0] * (max_weight_needed + 1)
    
    for price, weight in objects:
        for w in range(max_weight_needed, weight - 1, -1):
            if dp[w - weight] + price > dp[w]:
                dp[w] = dp[w - weight] + price
                
    total_family_value = sum(dp[p_weight] for p_weight in people)
    return total_family_value

def read_input():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    num_test_cases = int(input_data[idx])
    idx += 1
    
    for _ in range(num_test_cases):
        n = int(input_data[idx])
        idx += 1
        
        objects = []
        for _ in range(n):
            price = int(input_data[idx])
            weight = int(input_data[idx+1])
            objects.append((price, weight))
            idx += 2
            
        g = int(input_data[idx])
        idx += 1
        
        people = []
        for _ in range(g):
            people.append(int(input_data[idx]))
            idx += 1
            
        ans = solve_case(objects, people)
        print(ans)

read_input()