import sys

def get_highest_score(board, queens):
    highest = 0
    current_score = 0
    # cada board es un 8x8
    # queens son todas las soluciones posibles
    # sumar el valor de board de cada queen
    # mantener el highest obtenido
    # posicion es sgn yo: board[0-7][queens[0-len(queens)][0-7]]
    for i in range(len(queens)):
        current_score = 0
        for j in range(8):
            current_score += board[j][queens[i][j]]
            if current_score > highest:
                highest = current_score

    return highest


def check_valid_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i] == queens[j]:
                return False
            if abs(i - j) == abs(queens[i] - queens[j]):
                return False
    return True

def eight_queens_solutions():
    eight_queens = []
    
    def backtrack(solution):
        if len(solution) == 8:
            eight_queens.append(solution[:])
            return
        
        row = len(solution)
        for col in range(8):
            solution.append(col)
            if check_valid_queens(solution):
                backtrack(solution)
            solution.pop()
    
    backtrack([])
    return eight_queens


def read_input(infile):
    values = list(map(int, infile.read().split()))
    if not values:
        return
    
    idx = 0
    amount_of_boards = values[idx]
    idx += 1
    
    if amount_of_boards == 0 or amount_of_boards > 20:
        return

    possible_solutions = eight_queens_solutions()
    for b in range(amount_of_boards):
        board = []
        for row in range(8):
            row_data = values[idx:idx+8]
            board.append(row_data)
            idx += 8

        highest_score = get_highest_score(board, possible_solutions)

        print(f"{highest_score:5d}")

read_input(sys.stdin)

#variacion de la problema de las 8 reinas
#encontrar las soluciones de las 8 reinas primero (son conocidas)
#con esas configuraciones probar cuales posiciones suman mas
#un backtracking para las posiciones y lo otro es probar los valores con cada posible solucion