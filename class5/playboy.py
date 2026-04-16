import sys
from bisect import bisect_left, bisect_right

def read_input(infile):
    values = list(map(int, infile.read().split()))
    if not values:
        return
    
    chimps_amount = values[0]
    chimps_heights = values[1:1+chimps_amount]
    luchu_amount = values[1+chimps_amount]
    luchus_heights = values[1+chimps_amount+1:1+chimps_amount+1+luchu_amount]

    for x in luchus_heights:
        left = bisect_left(chimps_heights, x)
        right = bisect_right(chimps_heights, x)

        shorter_partner = chimps_heights[left - 1] if left > 0 else None
        taller_partner = chimps_heights[right] if right < len(chimps_heights) else None

        print(shorter_partner if shorter_partner is not None else "X",
              taller_partner if taller_partner is not None else "X")

read_input(sys.stdin)