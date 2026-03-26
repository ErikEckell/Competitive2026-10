import sys

def read_input(infile):
    values = list(map(int, infile.read().split()))
    if not values:
        return
    
    cases_count = values[0]
    current_case = 1
    idx = 1
    while cases_count > 0:
        is_valid = True

        a = values[idx]
        b = values[idx + 1]
        c = values[idx + 2]

        if a + b <= c:
            is_valid = False
        
        if a + c <= b:
            is_valid = False

        if b + c <= a:
            is_valid = False

        if is_valid:
            if (a == b == c):
                print(f"Case {current_case}: Equilateral")
            elif (a == b != c) or (a == c != b) or (b == c != a):
                print(f"Case {current_case}: Isosceles")
            else:
                print(f"Case {current_case}: Scalene")
        else:
            print(f"Case {current_case}: Invalid")

        idx += 3
        current_case += 1
        cases_count -= 1

read_input(sys.stdin)
