# SoloHalma.py
# Peg Solitaire, Solo Noble, Brainvita
# ULi160616, ULi160617

from copy import deepcopy

holes = [
[0,0,1,1,1,0,0],
[0,0,1,1,1,0,0],
[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],
[0,0,1,1,1,0,0],
[0,0,1,1,1,0,0],
]

stones = deepcopy(holes)
stones[3][3] = 0
drops = sum(sum(x) for x in stones) - 1

good = [[0 for j in i] for i in holes]
good[3][3] = 1

moves = []
count = 0

def mo(x0, y0, xo, yo):
    x1, y1 = x0 + xo, y0 + yo
    x2, y2 = x1 + xo, y1 + yo
    if (
        0 <= x2 < 7 and 
        0 <= y2 < 7 and
        stones[x1][y1] and
        holes[x2][y2] and
        not stones[x2][y2]
    ):
        stones[x0][y0] = 0
        stones[x1][y1] = 0
        stones[x2][y2] = 1
        moves.append((x0, y0, x2, y2))
        move()
        stones[x0][y0] = 1
        stones[x1][y1] = 1
        stones[x2][y2] = 0
        moves.pop()

def move():
    global count
    for x in range (7):
        for y in range (7):
            if stones[x][y]:
                mo(x, y,  1,  0)
                mo(x, y,  0,  1)
                mo(x, y, -1,  0)
                mo(x, y,  0, -1)
    if len(moves) == drops and stones == good:
        print(moves)
        count += 1

move()
print(count)
