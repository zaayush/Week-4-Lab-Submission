# -*- coding: utf-8 -*-
"""Week 4: Lab Submission (GitHub Version Control).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1chSTIez8Dk7kylX0I0vGs764mYVOzAd8
"""

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

def flood_fill(input_board, old, new, x, y):
    def recursive_ff(x, y):
        if (
            x < 0
            or x >= len(input_board)
            or y < 0
            or y >= len(input_board[0])
            or input_board[x][y] != old
        ):
            return

        input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]
        recursive_ff(x + 1, y)
        recursive_ff(x - 1, y)
        recursive_ff(x, y + 1)
        recursive_ff(x, y - 1)

    recursive_ff(x, y)
    return input_board


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....

modified_board = flood_fill(input_board=board, old="~", new=".", x=1, y=1)

for a in modified_board:
    print(a)

