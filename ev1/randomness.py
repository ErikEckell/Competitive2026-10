import sys

def read_input(infile):
    values = list(map(int, infile.read().split()))
    if not values:
        return
    
    idx = 0
    outputs = []
    while idx < len(values):
        r = values[idx]
        n = values[idx + 1]
        if r == 0 and n == 0:
            break

        idx += 2
        probs = []
        for _ in range(n):
            a = values[idx]
            b = values[idx + 1]
            probs.append((a, b))
            idx += 2

        best = float("inf")
        m = 1
        k = 0

        while True:
            k += 1
            m *= r

            assigned = 0
            for a, b in probs:
                assigned += (m * a) // b

            if assigned > 0:
                expected = (k * m) / assigned
                if expected < best:
                    best = expected

            if k >= best:
                break

        outputs.append(f"{best:.6f}")

    sys.stdout.write("\n".join(outputs))


read_input(sys.stdin)