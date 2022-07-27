from random import randrange
import argparse

parser = argparse.ArgumentParser(description='argparse greeting')
parser.add_argument('-s', '--size', help='size of the board you want to play', required=True)
args = parser.parse_args()

def print_board (table):
    print("Game board:")
    for row in table:
        for value in row:
            print("{}".format(value), end=" ")
        print()

def game_board (size):
    table_size = int(size)
    table = []
    for a in range(table_size):
        row = []
        for b in range(table_size):
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

def render_board(snake_positions, fruit_position, size=10):
    board = game_board(size)
    x, y = fruit_position
    board[x][y] = "@"
    for x, y in snake_positions:
        board[x][y] = "X"
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

def increase (coordinates, direction):
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

def movement_check(coordinates):
    if len(coordinates) == len(set(coordinates)):
        return False
    else:
        return True

def fruit(size):
    upper_number = int (size)
    coordinates=[]
    for i in range(2):
        coordinates.append(randrange(0,upper_number))
    return tuple(coordinates)

def player_input():
    player_move=input("Where do you want a snake to move now?\na - left, d - right, w - up, s - down\nend - to leave the game. ")
    while True:
        if player_move=="a" or player_move=="w" or player_move=="s" or player_move=="d" or player_move=="end":
            return player_move
            break
        else:
            player_move=input ("Incorrect input, please try again: ")

coordinates=[(0,0),(0,1),(0,2)]
table=game_board(args.size)
draw_board(table,coordinates)
print_board (table)

while True:
    flag = False
    coordinates_fruit=fruit(args.size)
    check = coordinates_fruit in coordinates
    if check:
        coordinates_fruit=fruit(args.size)
    else:
        while coordinates[-1] != coordinates_fruit:
            player_move=player_input()
            if player_move == "end":
                print ("Game is over!")
                flag = True
                break
            try:
                movement(coordinates, player_move)
            except ValueError:
                print ("Oh no! You crashed against the wall. You lost!")
                flag = True
                break
        
            try:
                table = render_board(coordinates,coordinates_fruit)
                result = movement_check (coordinates)
            except IndexError:
                print ("Oh no! You crashed against the wall. You lost!")
                flag = True
                break
            
            if result:
                print ("Oh no! You are bitting yourself. You lost!")
                flag = True
                break
            print_board (table)
        else:
            print ("Yammy! It is good for me! I will drow in the next step")
            player_move=player_input()
            if player_move == "end":
                print ("Game is over!")
                flag = True
                break
            try:
                increase(coordinates, player_move)
            except ValueError:
                flag = True
                print ("Oh no! You crashed against the wall. You lost!")
                break

            table = render_board(coordinates,coordinates_fruit)
            result = movement_check (coordinates)
            if result:
                print ("Oh no! You are bitting yourself. You lost!")
                flag = True
                break
            print_board (table)
    if flag == True:
            break
