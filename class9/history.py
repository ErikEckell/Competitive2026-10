import sys

def get_lis(seq):
    n = len(seq)
    if n == 0:
        return 0
        
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if seq[j] < seq[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    
    return max(dp)

def read_input():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        
        correct_pos = [0] * n
        for i in range(n):
            pos = int(input_data[idx]) - 1
            correct_pos[pos] = i
            idx += 1
            
        while idx < len(input_data):
            if idx + n <= len(input_data):
                is_new_case = False
                for k in range(n):
                    val = int(input_data[idx + k])
                    if val > n:
                        is_new_case = True
                        break
                
                if is_new_case:
                    break
            else:
                break
                
            student_pos = [0] * n
            for i in range(n):
                pos = int(input_data[idx]) - 1
                student_pos[pos] = i
                idx += 1
                
            transformed_seq = [0] * n
            for i in range(n):
                event = student_pos[i]
                transformed_seq[i] = correct_pos[event]
                
            print(get_lis(transformed_seq))

read_input()