
def game_board (size=10):
    table = []
    for a in range(size):
        row = []
        for b in range(size):
            row.append(".")
        table.append(row)
    return table

def print_board (table):
    print("Game board:")
    for row in table:
        for value in row:
            print("{}".format(value), end=" ")
        print()

def draw_board(table,coordinates):
    for i in coordinates:
        x_y=i
        for j in x_y:
            x=x_y[0]
            y=x_y[1]
        table[x][y]="X" 


def movement (coordinates, direction):
    last_spot = coordinates[-1]
    if direction == "s":
        change=last_spot[0]+1
        move=(change,last_spot[1])
        coordinates.append(move)
    if direction == "w":
        change=last_spot[0]-1
        move=(change,last_spot[1])
        coordinates.append(move)
    if direction == "d":
        change=last_spot[1]+1
        move=(last_spot[0],change)
        coordinates.append(move) 
    if direction == "a":
        change=last_spot[1]-1
        move=(last_spot[0],change)
        coordinates.append(move)
    coordinates.pop(0)                   


coordinates=[(0,0),(0,1),(0,2)]
while True:
    player_move=input ("Where do you want a snake to move now?\nChose between a - left, d - right, w - up, s - down or end - to leave the game. ")
    if player_move == "end":
        break
    movement(coordinates, player_move)
    table=game_board()
    draw_board(table, coordinates)
    print_board(table)
    
