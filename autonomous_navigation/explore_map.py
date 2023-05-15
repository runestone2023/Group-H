from random import randrange

def print_map(map, size_x, size_y):
    for y in range(size_y):
        for x in range(size_x):
            print(map[x][y], end='')
        print()





def track_map(size_x, size_y, init_pos_x, init_pos_y):
    map = [["X" for x in range(size_x)] for x in range(size_y)]

    map[init_pos_x][init_pos_y] = "R"

    print_map(map, size_x, size_y)

    moves = ["up", "down", "left", "right"]
    cur_x = init_pos_x
    cur_y = init_pos_y

    for i in range(10):
        next_move = moves[randrange(3)]
        print(next_move)
        if(next_move == "up" and cur_y > 0):
            map[cur_x][cur_y] = "_"
            map[cur_x][cur_y - 1] = "R"
            cur_x = cur_x
            cur_y = cur_y - 1 
        elif(next_move == "down" and cur_y < size_y):
            map[cur_x][cur_y] = "_"
            map[cur_x][cur_y +1] = "R"
            cur_x = cur_x
            cur_y = cur_y + 1 
        elif(next_move=="left" and cur_x > 0):
            map[cur_x][cur_y] = "_"
            map[cur_x - 1][cur_y] = "R"
            cur_x = cur_x - 1
            cur_y = cur_y
        elif(next_move=="right" and cur_x < size_x):
            map[cur_x][cur_y] = "_"
            map[cur_x + 1][cur_y] = "R"
            cur_x = cur_x + 1
            cur_y = cur_y
        else:
            print("skipping turn")

        print_map(map, size_x, size_y)

    # set target at initial position
    map[init_pos_x][init_pos_y] = "T"




if __name__ == '__main__':
    print()
    track_map(5,5,2,3)


