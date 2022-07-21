
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

table=game_board()
print (table)


def draw_board(table,coordinates):
    for i in coordinates:
        x_y=i
        for j in x_y:
            x=x_y[0]
            y=x_y[1]
        table[x][y]="X" 
    return table


def movement (coordinates, direction):
    last_spot = coordinates[-1]
    print (last_spot)
    if direction == "s":
        change=last_spot[0]+1
        move=(change,last_spot[1])
        coordinates.append(move)
    if direction == "n":
        change=last_spot[0]-1
        move=(change,last_spot[1])
        coordinates.append(move)
    if direction == "e":
        change=last_spot[1]+1
        move=(last_spot[0],change)
        coordinates.append(move) 
    if direction == "w":
        change=last_spot[1]-1
        move=(last_spot[0],change)
        coordinates.append(move)                   

coordinates=[(8,9),(0,0)]
movement(coordinates, 'e')
print(coordinates)
movement(coordinates, 'e')
print(coordinates)
movement(coordinates, 's')
print(coordinates)
movement(coordinates, 'n')
print(coordinates)

print (draw_board(table, coordinates))

print_board(table)