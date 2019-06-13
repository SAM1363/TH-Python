# EXAMPLES:
# move((1, 1, 10), (-1, 0)) => (0, 1, 10)
# move((0, 1, 10), (-1, 0)) => (0, 1, 5)
# move((0, 9, 5), (0, 1)) => (0, 9, 0)


def move(player, direction):
    x, y, hp = player
    x1, y1 = direction

    if x == 0 and x1 == -1:
        hp -= 5
    elif x == 9 and x1 == 1:
        hp -= 5
    elif y == 0 and y1 == -1:
        hp -= 5
    elif y == 9 and y1 == 1:
        hp -= 5
    else:
        x += x1
        y += y1

    return x, y, hp


def move2(player, direction):
    x, y, hp = player
    x1, y1 = direction
    if (x1+x == -1) or (x1+x == 10) or (y1+y == -1) or (y1+y == 10):
        hp -= 5
    else:
        x += x1
        y += y1

    return x, y, hp 

print(move((0, 9, 5), (0, 1)))