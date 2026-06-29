board = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3]
]

player_0 = input("Enter the name of the first player (X): ")
player_1 = 'AI'

def minimax(board, isMax):
    winner = checkWinner(board)
    if winner == 'O':
        return 1
    if winner == 'X':
        return -1
    
    full = True
    for i in board:
        for j in i:
            if j not in ('X', 'O'):
                full = False

    if full:
        return 0
    
    if isMax:
        best = -100

        for i in range(3):
            for j in range(3):
                if board[i][j] not in ('X', 'O'):
                    temp = board[i][j]
                    board[i][j] =  'O'
                    score = minimax(board, False)
                    board[i][j] = temp
                    best = max(best, score)

        return best
    else:
        best = 100
        for i in range(3):
            for j in range(3):
                if board[i][j] not in ('X', 'O'):
                    temp = board[i][j]
                    board[i][j] =  'X'
                    score = minimax(board, True)
                    board[i][j] = temp
                    best = min(best, score)

        return best


def aiTurn(board):
    best = -100
    move_i = None
    move_j = None
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ('O', 'X'):
                temp = board[i][j]
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = temp
                if score > best:
                    best = score
                    move_i = i
                    move_j = j
    if move_i is not None and move_j is not None:
        board[move_i][move_j] = 'O'

    return board

def checkWinner(board):
    LINES = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],

        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],

        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)],
    ]

    for i in LINES:
        r1, c1 = i[0]
        r2, c2 = i[1]
        r3, c3 = i[2]
        if board[r1][c1] == board[r2][c2] == board[r3][c3]:
            return board[r1][c1]
    
    return None
def printBoard(board):
    print('+---+---+---+')
    for i in board: 
        print(f'| {i[0]} | {i[1]} | {i[2]} |')
        print('+---+---+---+')

printBoard(board)

current_turn = 0

while True:
    print(f"{globals()[f'player_{current_turn}']}'s turn!")
    if current_turn == 0:
        choice = int(input('Enter the position no: '))
        
        row = (9 - choice) // 3
        col = (choice  - 1) % 3
        if board[row][col] == 'X' or board[row][col] == 'O':
            print('dont try to cheat!')
            continue
        else:
            board[row][col] = 'X' if current_turn == 0 else 'O'
    else:
        board = aiTurn(board)
    current_turn = 1 - current_turn
    printBoard(board)
    Winner = checkWinner(board)
    if (Winner):
        print(f'{Winner} has won the game!')
        break
    full = True
    for i in board:
        for j in i:
            if j not in ('O', 'X'):
                full = False
    if full:
        print('Draw')
        break