from random import randrange

def print_board (table):
    print("Game board:")
    for row in table:
        for value in row:
            print("{}".format(value), end=" ")
        print()

def game_board (size=10):
    table = []
    for a in range(size):
        row = []
        for b in range(size):
            row.append(".")
        table.append(row)
    return table

def draw_board(board,coordinates):
    for i in coordinates:
        x_y=i
        for j in x_y:
            x=x_y[0]
            y=x_y[1]
        if board[x][y]!="X":
            board[x][y]="X" 
        else:
            raise ValueError
    return board

def movement (coordinates, direction):
    last_spot = coordinates[-1]
    if direction == "s":
        change=last_spot[0]+1
        move=(change,last_spot[1])
        coordinates.append(move)
    if direction == "w":
        change=last_spot[0]-1
        if change == -1:
            raise ValueError
        move=(change,last_spot[1])
        coordinates.append(move)
    if direction == "d":
        change=last_spot[1]+1
        move=(last_spot[0],change)
        coordinates.append(move) 
    if direction == "a":
        change=last_spot[1]-1
        if change == -1:
            raise ValueError       
        move=(last_spot[0],change)
        coordinates.append(move)
    coordinates.pop(0)                   

def fruit():
    coordinates=[]
    for i in range(2):
        coordinates.append(randrange(0,9))
    return coordinates

def fruit_on_board(table, coordinates):
    for i in coordinates:
        x=coordinates[0]
        y=coordinates[1]
    if table[x][y]=="X":
        raise ValueError
    if not "@" in table:
        table[x][y]="@"
    return table


coordinates=[(0,0),(0,1),(0,2)]
table=game_board()
coordinates_fruit=fruit()


try:
    table = fruit_on_board(table,coordinates_fruit)
    print_board (table)
except ValueError:
    print("error")
    coordinates_fruit=fruit()
    fruit_on_board(table,coordinates_fruit) 
    print_board(table)

for i in range(5):
    player_move=input (
        "Where do you want a snake to move now?\n\
        Chose between a - left, d - right, w - up, s - down\n\
        or end - to leave the game. ")
    if player_move == "end":
        break
    try:
        movement(coordinates, player_move)
        print (coordinates)
    except ValueError:
        print ("Oh no! You crashed against the wall. You lost!")
        break
    
    print ("table+fruit",table)
    table2=draw_board(table, coordinates)
    print ("table+fruit 2 time",table)
    print ("changed table",table2)
    # except ValueError:
    #     print ("Oh no! You are bitting yourself. You lost!")
    #     break
    # except IndexError:
    #     print ("Oh no! You crashed against the wall. You lost!")
    #     break
    print_board(table2)
