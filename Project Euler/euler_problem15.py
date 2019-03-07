END_X = 10
END_Y = 10

moves = ["R","D"] # right and down

def search_path(x, y, turn):
    term = 0
    for move in moves:
        #print("x", x, "y", y, "turn", turn, "term", term)
        if move == "R":
            if x >= END_X:
                continue
            # move right
            term += search_path(x+1, y, turn+1)
        if move == "D":
            if y >= END_Y:
                continue
            # move down
            term += search_path(x, y+1, turn+1)

    if x == END_X and y == END_Y:
        #print("termination", "x", x, "y", y, "turn", turn)
        return 1

    # did not terminate
    return term

# start
print("result:", search_path(0, 0, 0))
