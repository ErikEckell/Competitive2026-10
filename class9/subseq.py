import sys

def solve_sequence(nums):
    if not nums:
        return 0
    
    current_max = nums[0]
    current_min = nums[0]
    global_max = nums[0]
    
    for x in nums[1:]:
        temp_max = max(x, x * current_max, x * current_min)
        current_min = min(x, x * current_max, x * current_min)
        current_max = temp_max
        
        if current_max > global_max:
            global_max = current_max
            
    return global_max

def read_input():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    current_sequence = []
    
    while idx < len(input_data):
        val = int(input_data[idx])
        idx += 1
        
        if val == -999999:
            print(solve_sequence(current_sequence))
            current_sequence = []
        else:
            current_sequence.append(val)

read_input()