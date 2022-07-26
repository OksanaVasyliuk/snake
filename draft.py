from random import randrange

# def print_board (table):
#     print("Game board:")
#     for row in table:
#         for value in row:
#             print("{}".format(value), end=" ")
#         print()

# table = [
#     ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
#      ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], 
#      ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],       ['.', '.', '.', '.', '.', 'X', '.', '.', '.', '.'], 
#       ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

# def fruit ():
#     coordinates=[]
#     for i in range(2):
#         coordinates.append(randrange(0,9))
#     return coordinates

# def fruit_on_board(table, coordinates):
#     for i in coordinates:
#         x=coordinates[0]
#         y=coordinates[1]
#     if table[x][y]!="X":
#         table[x][y]="@"
#     else:
#         raise ValueError

# while True:
#     coordinates=fruit()
#     try:
#         fruit_on_board(table,coordinates)
#     except ValueError:
#         print("error")
#         coordinates=fruit()
#         fruit_on_board(table,coordinates)
#     print_board(table)



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

# def draw_board(table,coordinates):
#     for i in coordinates:
#         x_y=i
#         for j in x_y:
#             x=x_y[0]
#             y=x_y[1]
#         if table[x][y]!="X":
#             table[x][y]="X" 
#         else:
#             raise ValueError


# def draw_board(coordinates,size=10):
#     table = []
#     for a in range(size):
#         row = []
#         for b in range(size):
#             row.append(".")
#         table.append(row)
#     for i in coordinates:
#         x_y=i
#         for j in x_y:
#             x=x_y[0]
#             y=x_y[1]
#         if table[x][y]!="X":
#             table[x][y]="X" 
#         else:
#             raise ValueError
#     return table
# 

# def draw_board(coordinates,size=10):
#     table = []
#     for a in range(size):
#         row = []
#         for b in range(size):
#             row.append(".")
#         table.append(row)
#     for i in coordinates:
#         x_y=i
#         for j in x_y:
#             x=x_y[0]
#             y=x_y[1]
#         if table[x][y]!="X":
#             table[x][y]="X" 
#         else:
#             raise ValueError
#     return table

# def fruit():
#     coordinates=[]
#     for i in range(2):
#         coordinates.append(randrange(0,3))
#     return tuple(coordinates)

# def render_board(snake_positions, fruit_position, size=3):
#     board = game_board(size)
#     x, y = fruit_position
#     board[x][y] = "@"
#     for x, y in snake_positions:
#         board[x][y] = "X"
#     return board



# coordinates=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)]


# while True:
#     coordinates_fruit=fruit()
#     check = coordinates_fruit in coordinates
#     print (check)
#     if check:
#         coordinates_fruit=fruit()
#         print (coordinates_fruit)
#     else:
#         table= render_board(coordinates,coordinates_fruit)
#         print_board (table)
#         break

coordinates = [(5, 3), (6, 3), (6, 2)]
coordinates=[((coordinates[0][0]-1),coordinates[0][1])+coordinates]
print (coordinates)
# coordinates_fruit = (6, 2)
# if coordinates[-1] != coordinates_fruit:
#     print ("la")
# else:
#     print ("la-la")

