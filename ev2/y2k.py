# si el año tiene 12 meses
# el primer reporto contiene  del 1-5
# el segundo del 2-6
# el tercer del 3-7
# y asi sucesivamente
# 8-12

# me dan un s y un d
# cada mes puede ser o s o d, no se cual es cual
# yo se que la sumatoria de de los meses es deficit
# (1-5, 2-6, 3-7, 4-8, 5-9, 6-10, 7-11, 8-12; son todos deficit sus sumas)
# la pregunta es si del mes 1-12 hubo superavit o deficit

# cada uno de los 8 posts la sumatoria de los meses debe ser deficit
# se debe buscar la mejor combinacion de s y d donde se cumpla lo anterior
# tal que la sumatoria de los meses 1-12 sea el mayor superavit posible
# caso contrario es deficit
import sys

def generate_year(combination, s, d):
    year = []
    for is_surplus in combination:
        if is_surplus == 1:
            year.append(s)
        else:
            year.append(-d)
    return year

def is_valid_year(year):
    for start in range(8):
        window = year[start:start+5]
        window_sum = sum(window)
        if window_sum >= 0:
            return False
    return True

def get_bit(number, position):
    return (number >> position) & 1

def solve(s, d):
    max_surplus = None
    
    for combination_number in range(4096):
        combination = []
        for bit_position in range(12):
            bit_value = get_bit(combination_number, bit_position)
            combination.append(bit_value)
        
        year = generate_year(combination, s, d)
        
        if is_valid_year(year):
            total_annual = sum(year)
            
            if max_surplus is None or total_annual > max_surplus:
                max_surplus = total_annual
    
    if max_surplus is not None and max_surplus > 0:
        print(max_surplus)
    else:
        print("Deficit")

def read_input(infile):
    values = list(map(int, infile.read().split()))
    if not values:
        return
    
    idx = 0
    while idx < len(values):
        s = values[idx]
        d = values[idx + 1]
        idx += 2
        solve(s, d)

read_input(sys.stdin)