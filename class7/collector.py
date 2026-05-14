import sys

def read_input(infile):
    values = list(map(int, infile.read().split()))
    if not values:
        return
    idx = 0

read_input(sys.stdin)