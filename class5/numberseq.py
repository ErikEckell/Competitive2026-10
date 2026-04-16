import sys
from bisect import bisect_left

num_prefix = [0]
seq_prefix = [0]


def ensure_prefixes(target_pos):
    n = len(num_prefix) - 1
    while seq_prefix[-1] < target_pos:
        n += 1
        num_prefix.append(num_prefix[-1] + len(str(n)))
        seq_prefix.append(seq_prefix[-1] + num_prefix[-1])


def solve(x):
    ensure_prefixes(x)

    k = bisect_left(seq_prefix, x)
    pos_in_block = x - seq_prefix[k - 1]

    m = bisect_left(num_prefix, pos_in_block, 1, k + 1)
    pos_in_number = pos_in_block - num_prefix[m - 1] - 1

    print(str(m)[pos_in_number])
    

def read_input(infile):
    values = list(map(int, infile.read().split()))
    if not values:
        return
    
    cases = values[0]
    
    idx = 1
    while cases > 0:
        solve(values[idx])
        idx += 1
        cases -= 1

read_input(sys.stdin)