import sys
from bisect import bisect_left

def generate_candidates():

    limit = 2**31
    candidates = set()

    power_of_2 = 1
    while power_of_2 <= limit:
        power_of_3 = 1
        while power_of_2 * power_of_3 <= limit:
            candidates.add(power_of_2 * power_of_3)
            power_of_3 *= 3
        power_of_2 *= 2
    
    return sorted(candidates)

all_candidates = generate_candidates()

def solve(value):
    idx = bisect_left(all_candidates, value)
    if idx < len(all_candidates) and all_candidates[idx] >= value:
        return all_candidates[idx]
    return all_candidates[idx + 1]

def read_input(infile):
    values = list(map(int, infile.read().split()))
    if not values:
        return
    
    for value in values:
        #print(value)
        if value == 0:
            break
        print(solve(value))

read_input(sys.stdin)