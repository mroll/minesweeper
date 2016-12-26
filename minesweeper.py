from random import randint
import re

# Board:
# 2d matrix
# each element can either be a bomb or not, and it can either be hidden or not.
# let's say squares w/ bombs will be 'b'
# squares w/out bombs will be 0 if hidden and 1 if not.
# when we go to display the board, we show all hidden squares as '.'s
# and all non-hidden squares as the number of adjacent bombs.

def dims(board):
    return [len(board), len(board[0])]

def nrows(board):
    return len(board)

def ncols(board):
    return len(board[0])

def above(board, row, col):
    if row > 0:
        return board[row-1][col]

def below(board, row, col):
    if row < nrows(board)-1:
        return board[row+1][col]

def left(board, row, col):
    if col > 0:
        return board[row][col-1]

def right(board, row, col):
    if col < ncols(board)-1:
        return board[row][col+1]

def diag_upright(board, row, col):
    if row > 0 and col < ncols(board)-1:
        return board[row-1][col+1]

def diag_upleft(board, row, col):
    if row > 0 and col > 0:
        return board[row-1][col-1]

def diag_downright(board, row, col):
    if row < nrows(board)-1 and col < ncols(board)-1:
        return board[row+1][col+1]

def diag_downleft(board, row, col):
    if row < nrows(board)-1 and col > 0:
        return board[row+1][col-1]

directions = [above, below, left, right, diag_upright, diag_upleft, diag_downright, diag_downleft]

def bombs_adj(board, row, col):
    global directions
    adjacents = [dir(board, row, col) for dir in directions]
    return adjacents.count('b')

def display_char(board, row, col):
    char = board[row][col]
    if char == 'b' or char == 0:
        return '.'

    return str(bombs_adj(board, row, col))

def display_char_transparent(board, row, col):
    if board[row][col] == 0:
        return '.'
    if board[row][col] == 'b':
        return 'b'

    return str(bombs_adj(board, row, col))

def display(board):
    nrows, ncols = dims(board)

    print '  ' + ' '.join([str(i) for i in range(ncols)])
    for row in range(nrows):
        print str(row) + ' ' + ' '.join([display_char(board, row, col) for col in range(ncols)])


def display_transparent(board):
    nrows, ncols = dims(board)

    for row in range(nrows):
        print ' '.join([display_char_transparent(board, row, col) for col in range(ncols)])

def choose_rand_k(k, n):
    bigrand = 20 * n
    select = k
    remaining = n

    selected = []

    for i in range(n):
        if (randint(0, bigrand) % remaining) < select:
            selected.append(i)
            select -= 1

        remaining -= 1

    return selected

def make_board(n, m, bombs):
    squares = [0] * (n*m)

    bomb_squares = choose_rand_k(bombs, (n*m))
    for bs in bomb_squares:
        squares[bs] = 'b'

    return [squares[i*m:(i*m)+m] for i in range(n)]

def adjacent_coords(board, row, col):
    coords = []
    if row > 0:
        coords.append([row-1, col])
    if row < nrows(board)-1:
        coords.append([row+1, col])
    if col > 0:
        coords.append([row, col-1])
    if col < ncols(board)-1:
        coords.append([row, col+1])
    if row > 0 and col < ncols(board)-1:
        coords.append([row-1, col+1])
    if row > 0 and col > 0:
        coords.append([row-1, col-1])
    if col > 0 and row < nrows(board)-1:
        coords.append([row+1, col-1])
    if col < ncols(board)-1 and row < nrows(board)-1:
        coords.append([row+1, col+1])

    return coords

def reveal(board, row, col):
    if board[row][col] is 1:
        return board
    
    if bombs_adj(board, row, col) is not 0:
        board[row][col] = 1
        return board

    board[row][col] = 1
    for i, j in adjacent_coords(board, row, col):
        board = reveal(board, i, j)

    return board

def stepped_on_bomb(board):
    for row in board:
        for col in row:
            if col == 'x':
                return True

    return False

def move(board, row, col):
    global ERRLOSE

    if board[row][col] == 'b':
        board[row][col] = 'x'
        return board

    return reveal(board, row, col)

def squares_left(board):
    for row in board:
        for col in row:
            if col == 0:
                return True

    return False

def input_func(board):
    nrows, ncols = dims(board)
    prompt = "Enter coords ([0-{}][0-{}]): ".format(nrows-1, ncols-1)
    matchstr = r"^[0-{}][0-{}]$".format(nrows-1, ncols-1)

    def get_input():
        row, col = [-1, -1]

        while (row < 0 or row > nrows-1) or (col < 0 or col > ncols-1):
            inp = raw_input(prompt)

            if not re.match(matchstr, inp):
                continue
            
            row, col = map(int, list(inp))

        return [row, col]

    return get_input

def main():
    board = make_board(9, 9, 20)
    get_input = input_func(board)

    while squares_left(board):
        display(board)
        row, col = get_input()

        board = move(board, row, col)
        if stepped_on_bomb(board):
            display_transparent(board)
            
            print "BOOM!"
            print "You lose :("
            return

    print "YAY!"
    print "You win :)"
    

ERRLOSE = -1

main()
