import json

MAX_X_Y = (10,10)

def get_neigbors(cell):
    (x,y) = cell
    return [(x-1,y),(x+1,y),(x,y-1),(x,y+1),
           (x-1,y-1),(x+1,y-1),(x-1,y+1),(x+1,y+1)]

def edge (cell, board):
    for (x,y) in get_neigbors(cell):
        board[(x,y)] = board.get((x,y), 0)

def check(cell, board):
    life = 0
    for (x,y) in get_neigbors(cell):
        if board.get((x,y), 0):
            life += 1
    return life

def advance(board):
    for cell in board.copy():
        edge(cell, board)

    nboard = {}
    for cell in board:
            (x,y) = cell
            life = check(cell, board)
            # live cell ?
            if board.get((x,y), 0):
                if life == 2 or life == 3:
                    nboard[(x,y)] = 1
            # dead cell ?
            elif life == 3:
                nboard[(x,y)] = 1
    return nboard

def display(board):
    for y in range (0, MAX_X_Y[0]):
        for x in range (0, MAX_X_Y[1]):
            print('',board.get((x,y), '-'),'', end='')
        print()
    print()


def generate_json(board):
    json_list = []
    for key in board:
        if board.get(key, 0):
            (x,y) = key
            # encode coordinates
            json_list.append(dict([("x", x),("y", y),("value", board[key])]))
    return(json.dumps(json_list, indent=4, separators=(',',':')))

def test_code():
    # intialize board with glider
    board = {(1,0):1, (2,1):1, (0,2):1, (1,2):1, (2,2):1}

    # advance
    for n in range(10):
        print("Move #", n+1)
        #display(board)
        print(generate_json(board))
        board = advance(board)

# main
if __name__ == '__main__':
    test_code()
