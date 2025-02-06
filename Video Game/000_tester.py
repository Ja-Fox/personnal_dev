def master_map():
    map_height = 10
    map_width = 10
    player_x,player_y = 0,0 
    map_layout = [
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "]
    ]
    return map_height,map_width,map_layout,player_x,player_y

def display_map(map_height, map_width ,map_layout, player_x, player_y):
    print("+---" * map_width + "+")
    for y in range(map_height):
        row = '|'
        for x in range(map_width):
            if x == player_x and y == player_y:
                row += 'X  |'
            else:
                continue
        print(row)
        print('+---' * map_width + '+')


map_height,map_width,map_layout,player_x,player_y = master_map()
display_map(map_height,map_width,map_layout,player_x,player_y)