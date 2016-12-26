# minesweeper

A simple minesweeper in python.

## gameplay

Run the game with the python interpreter.

    matt@fitz[17:39:15 ~/src/python/minesweeper]δ python minesweeper.py

The current board will be displayed at every turn. To move, input a
two digit string where the first digit is the row index and the second
digit is the column index. Indices are zero-indexed.

Example game:
    
      0 1 2 3 4 5 6 7 8
    0 . . . . . . . . .
    1 . . . . . . . . .
    2 . . . . . . . . .
    3 . . . . . . . . .
    4 . . . . . . . . .
    5 . . . . . . . . .
    6 . . . . . . . . .
    7 . . . . . . . . .
    8 . . . . . . . . .
    Enter coords ([0-8][0-8]): 45
      0 1 2 3 4 5 6 7 8
    0 . . . . . . . . .
    1 . . . . . . . . .
    2 . . . . . . . . .
    3 . . . . . . . . .
    4 . . . . . 3 . . .
    5 . . . . . . . . .
    6 . . . . . . . . .
    7 . . . . . . . . .
    8 . . . . . . . . .
    Enter coords ([0-8][0-8]): 23
      0 1 2 3 4 5 6 7 8
    0 . . . . . . . . .
    1 . . . . . . . . .
    2 . . . 3 . . . . .
    3 . . . . . . . . .
    4 . . . . . 3 . . .
    5 . . . . . . . . .
    6 . . . . . . . . .
    7 . . . . . . . . .
    8 . . . . . . . . .
    Enter coords ([0-8][0-8]): 80
      0 1 2 3 4 5 6 7 8
    0 . . . . . . . . .
    1 . . . . . . . . .
    2 . . . 3 . . . . .
    3 . . . . . . . . .
    4 . . . . . 3 . . .
    5 . . . . . . . . .
    6 . . . . . . . . .
    7 1 2 . . . . . . .
    8 0 1 . . . . . . .
    Enter coords ([0-8][0-8]): 08
      0 1 2 3 4 5 6 7 8
    0 . . . . . . . 1 0
    1 . . . . . . . 2 1
    2 . . . 3 . . . . .
    3 . . . . . . . . .
    4 . . . . . 3 . . .
    5 . . . . . . . . .
    6 . . . . . . . . .
    7 1 2 . . . . . . .
    8 0 1 . . . . . . .
    Enter coords ([0-8][0-8]): 88
    . . . . . . . 1 0
    . b b . . . b 2 1
    . . . 3 b b . b .
    b . . . b . . . b
    . . b . b 3 . b .
    . b . b . . b b .
    b . . . . . b . .
    1 2 . . . . . . .
    0 1 b . . . . . 0
    BOOM!
    You lose :(