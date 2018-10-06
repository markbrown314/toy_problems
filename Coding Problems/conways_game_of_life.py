MAX_X = 10
MAX_Y = 10

def check(board, coord_list):
    life = 0
    for coord in coord_list:
        if (coord[0] >= MAX_X or coord[1] >= MAX_Y
            or coord[0] < 0 or coord[1] < 0):
            continue
        if board[coord[0]][coord[1]]:
            life += 1
    return life

def advance(board):
    nboard = [[0 for x in range(MAX_X)] for y in range(MAX_Y)]

    for y in range(0, MAX_Y):
        for x in range (0, MAX_X):
            neighb_list = [(x-1,y),(x+1,y),(x,y-1),(x,y+1),
                           (x-1,y-1),(x+1,y-1),(x-1,y+1),(x+1,y+1)]
            life = check(board, neighb_list)

            # live cell
            if board[x][y]:
                if life < 2:
                    nboard[x][y] = 0
                elif life == 2 or life == 3:
                    nboard[x][y] = 1
                elif life > 3:
                    nboard[x][y] = 0
            # dead cell
            elif life == 3:
                nboard[x][y] = 1

    return nboard

def display(board):
    for y in range (0, MAX_Y):
        for x in range (0, MAX_X):
            print('', board[x][y], '', end ='')
        print()
    print()

def test_code():
    # intialize board
    board = [[0 for x in range(MAX_X)] for y in range(MAX_Y)]

    # render glider
    board[1][0] = 1
    board[2][1] = 1
    board[0][2] = 1
    board[1][2] = 1
    board[2][2] = 1

    # advance
    for n in range(10):
        print("move #", n+1)
        display(board)
        board = advance(board)

# main
if __name__ == '__main__':
    test_code()
