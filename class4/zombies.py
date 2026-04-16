# ver si el pajaro como de insecto o no
# similar al primero de la clase
# partir de una sol vacia []
# expandirla con 0 o 1 y luego verificar si es valida o no
# len(solution) =
# cmin <= sum(solution) <= cmax
# backtracking 
import sys

def extend_solution(solution, insects):

    if len(solution) < len(insects):
        return [solution + [0], solution + [1]]
    return []

def get_weight(solution, insects):
    return sum(solution[i] * insects[i] for i in range(len(solution)))

def process_solution(solution, insects):
    weight = get_weight(solution, insects)
    print("Sallow swallow swallows.")

def is_solution(cmin, cmax, solution, insects):
    if len(solution) != len(insects):
        return False
    weight = get_weight(solution, insects)
    return cmin <= weight <= cmax

def test_solution(cmin, cmax, solution, insects):
    current_weight = get_weight(solution, insects)
    
    if current_weight > cmax:
        return False
    
    if len(solution) == len(insects):
        return cmin <= current_weight <= cmax
    
    remaining_insects = insects[len(solution):]
    max_possible = current_weight + sum(remaining_insects)
    
    return max_possible >= cmin

def backtracking(cmin, cmax, insects, solution=[]):
    if is_solution(cmin, cmax, solution, insects):
        process_solution(solution, insects)
        return True
    else:
        found_solution = False
        for a_extended in extend_solution(solution, insects):
            if test_solution(cmin, cmax, a_extended, insects):
                if backtracking(cmin, cmax, insects, a_extended):
                    found_solution = True
                    break
        return found_solution

def read_input(infile):
    values = list(map(int, infile.read().split()))
    if not values:
        return
    
    idx = 0
    amount_of_swallows = values[idx]
    idx += 1
    
    if amount_of_swallows == 0 or amount_of_swallows > 30:
        return
    
    for s in range(amount_of_swallows):
        insects = []
        cmin = values[idx]
        cmax = values[idx + 1]
        amount_of_insects = values[idx + 2]
        for i in range(amount_of_insects):
            insect = values[idx + 3 + i]
            insects.append(insect)
        idx += amount_of_insects + 3
    
        found = backtracking(cmin, cmax, insects)
        if not found:
            print("Sallow swallow wallows in dust.")

read_input(sys.stdin)