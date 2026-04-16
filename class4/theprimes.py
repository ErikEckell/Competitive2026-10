# similar a sudoku
# numeros en columnas, filas y diagonales deben ser primos 
# y la suma de estos deben dar el mismo valor (en cada fila, columna y diagonal)
# colocar numeros del 1 al 9 en cada casilla
# similar a sudoku pero con primos y sumas iguales (cambia un poco el alogritmo nomas)
import sys
from itertools import permutations

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_valid_rows(prime_sum):
    """Pre-computar todas las filas válidas (números de 5 dígitos primos con suma correcta)"""
    valid_rows = []
    # Generar todas las combinaciones de 5 dígitos que sumen prime_sum
    def backtrack_row(row, remaining_sum):
        if len(row) == 5:
            if remaining_sum == 0:
                num = int(''.join(map(str, row)))
                if is_prime(num):
                    valid_rows.append(tuple(row))
            return
        
        # Primer dígito debe ser 1-9, resto puede ser 0-9
        min_digit = 1 if len(row) == 0 else 0
        for digit in range(min_digit, 10):
            if digit <= remaining_sum:
                backtrack_row(row + [digit], remaining_sum - digit)
    
    backtrack_row([], prime_sum)
    return valid_rows

def is_solution(solution, prime_sum):
    # Verificar una solución completa
    for i in range(5):
        row_sum = sum(solution[i])
        if row_sum != prime_sum:
            return False
        row_number = int(''.join(map(str, solution[i])))
        if not is_prime(row_number):
            return False
        
    for j in range(5):
        col = [solution[i][j] for i in range(5)]
        col_sum = sum(col)
        if col_sum != prime_sum:
            return False
        col_number = int(''.join(map(str, col)))
        if not is_prime(col_number):
            return False
    
    diag1 = [solution[i][i] for i in range(5)]
    diag1_sum = sum(diag1)
    if diag1_sum != prime_sum:
        return False
    diag1_number = int(''.join(map(str, diag1)))
    if not is_prime(diag1_number):
        return False
    
    diag2 = [solution[i][4 - i] for i in range(5)]
    diag2_sum = sum(diag2)
    if diag2_sum != prime_sum:
        return False
    diag2_number = int(''.join(map(str, diag2)))
    if not is_prime(diag2_number):
        return False
        
    return True

def backtracking(rows_so_far, prime_sum, valid_rows, solutions, first_digit):
    """Backtracking por filas en lugar de dígitos"""
    if len(rows_so_far) == 5:
        solution = rows_so_far
        if is_solution(solution, prime_sum):
            solutions.append([list(row) for row in solution])
        return
    
    current_row_idx = len(rows_so_far)
    
    for row in valid_rows:
        # Si es la primera fila, verificar que comience con first_digit
        if current_row_idx == 0 and row[0] != first_digit:
            continue
        
        rows_so_far.append(row)
        
        # Validación parcial: verificar columnas y diagonales que se completan
        valid = True
        
        # Verificar columnas que están completas (solo en última fila)
        if current_row_idx == 4:
            for j in range(5):
                col = [rows_so_far[i][j] for i in range(5)]
                col_sum = sum(col)
                if col_sum != prime_sum:
                    valid = False
                    break
                col_number = int(''.join(map(str, col)))
                if not is_prime(col_number):
                    valid = False
                    break
            
            # Verificar diagonales (solo si está completo)
            if valid:
                diag1 = [rows_so_far[i][i] for i in range(5)]
                diag1_sum = sum(diag1)
                if diag1_sum != prime_sum:
                    valid = False
                else:
                    diag1_number = int(''.join(map(str, diag1)))
                    if not is_prime(diag1_number):
                        valid = False
            
            if valid:
                diag2 = [rows_so_far[i][4 - i] for i in range(5)]
                diag2_sum = sum(diag2)
                if diag2_sum != prime_sum:
                    valid = False
                else:
                    diag2_number = int(''.join(map(str, diag2)))
                    if not is_prime(diag2_number):
                        valid = False
        
        if valid:
            backtracking(rows_so_far, prime_sum, valid_rows, solutions, first_digit)
        
        rows_so_far.pop()

def read_input(infile):
    values = list(map(int, infile.read().split()))
    if not values:
        return
    
    prime_sum = values[0]
    first_digit = values[1]

    # Pre-computar todas las filas válidas
    valid_rows = get_valid_rows(prime_sum)
    
    solutions = []
    backtracking([], prime_sum, valid_rows, solutions, first_digit)
    
    # Ordenar soluciones
    solutions.sort()
    
    # Imprimir soluciones
    for sol in solutions:
        for row in sol:
            print(''.join(map(str, row)))
        print()  # Salto de línea después de cada solución

read_input(sys.stdin)