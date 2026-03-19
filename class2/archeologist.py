from sys import stdin
from math import log2, ceil

LOG2_10 = log2(10)
EPS = 1e-12
mem_arch = {}


def archeologist(n):
    if n in mem_arch:
        return mem_arch[n]

    digits = len(str(n))
    missing = digits + 1
    lower_prefix = log2(n)
    upper_prefix = log2(n + 1)

    while True:
        lower = lower_prefix + missing * LOG2_10
        upper = upper_prefix + missing * LOG2_10
        k = ceil(lower - EPS)

        if k < upper - EPS:
            mem_arch[n] = k
            return k

        missing += 1


for line in stdin.readlines():
    n = int(line.strip())
    print(archeologist(n))

