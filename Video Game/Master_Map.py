def master_map(starting_location):
    print(f"""
    +---+---+---+---+---+---+---+--+
    | BOSS  |       |              |
    +       |       +              +
    |    __/        |              |
    +___/           +              +
    |               |              |
    +               +              +
    |               |              |
    +               +              +
    |               |              |
    +               +              +
    |               |              |
    +---+---+---+---+---+---+---+--+
    |               |              |
    +               +              +
    |               |              |
    +               +              +
    |               |              |
    +               +              +
    |               |              |
    +               +              +
    |               |              |
    +               +              +
    |               |              |
    +---+---+---+---+---+---+---+--+

    You begin at {starting_location}""")


def map_check():
    print(f"""
    +---+---+---+---+---+---+---+--+
    | BOSS  |       |              |
    +       |       +              +
    |    __/        |              |
    +___/           +              +
    |               |              |
    +               +              +
    |               |              |
    +               +              +
    |               |              |
    +               +              +
    |               |              |
    +---+---+---+---+---+---+---+--+
    |               |              |
    +               +              +
    |               |              |
    +               +              +
    |               |              |
    +               +              +
    |               |              |
    +               +              +
    |               |              |
    +               +              +
    |               |              |
    +---+---+---+---+---+---+---+--+

""")
    


# def master_map():
#     map_height = 10
#     map_width = 10
#     player_x,player_y = 0, 0 #import from character creation function
#     map_layout = [
#         [" "," "," "," "," "," "," "," "," "," "],
#         [" "," "," "," "," "," "," "," "," "," "],
#         [" "," "," "," "," "," "," "," "," "," "],
#         [" "," "," "," "," "," "," "," "," "," "],
#         [" "," "," "," "," "," "," "," "," "," "],
#         [" "," "," "," "," "," "," "," "," "," "],
#         [" "," "," "," "," "," "," "," "," "," "],
#         [" "," "," "," "," "," "," "," "," "," "],
#         [" "," "," "," "," "," "," "," "," "," "],
#         [" "," "," "," "," "," "," "," "," "," "]
#     ]
#     return map_height,map_width,map_layout

# def display_map(map_height,map_width,player_x,player_y,map_layout):
#     print("+---" * map_width + "+")
#     for y in range(map_height):
#         row = '|'
#         for x in range(map_width):
#             if x == player_x and y == player_y:
#                 row += 'X  |'
#             else:
#                 row += f' {map_layout,[y][x]:<3}|'
#         print(row)
#         print('+---' * map_width + '+')