from sys import stdin
from unicodedata import digit

max_n_value = 2**32
aux = False

def archeologist(n, num_digits):
    str_n = str(n)
    for i in range(0, max_n_value + 1):
        power_of_2 = 2 ** i
        str_power = str(power_of_2)

        for j in range(0, num_digits):
            n_digit = int(str_n[j]) if j < len(str_n) else 0
            pow_digit = int(str_power[j]) if j < len(str_power) else 0
            if(n_digit == pow_digit):
                aux = True
            else:
                aux = False

            #print(f'pow: {power_of_2} - n_digit: {n_digit} - pow_digit: {pow_digit} - aux: {aux}')
             
        if(len(str(2**i)) >= (num_digits*2+1) and aux):
            print(i)
            break

for line in stdin.readlines():
    line = (line.strip())
    num_digits = len(line)
    line = int(line)

    archeologist(line, num_digits)
    #print(f"{line} -> {archeologist(line, num_digits)}")
