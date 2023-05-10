import subprocess
import os
import time
import csv
import json
from PIL import Image
from numpy import asarray
# from output2commands.csv2json import csv2json
# import output2commands.main as out
# import autonomous_navigation
import output2commands
   


if __name__ == "__main__":
    # read map to pass to the a star algorithm
    image = Image.open('obstacle_course_images/map_1.png')

    # convert to numpy array for iteration over image
    array_map = asarray(image)

    # shape
    # print(array_map.shape)
    map_shape = array_map.shape

    # data
    # print(array_map)

    num_of_goals = 0
    num_of_robots = 0
    goal_x = -1
    goal_y = -1
    robot_x = -1
    robot_y = -1

    obstacle_arr = []

    # iterate through image and check pixels
    for x in range(map_shape[0]):
        for y in range(map_shape[1]):

            # check for green -> 0 255 0 -> goal
            if array_map[x][y][0] == 0 and array_map[x][y][1] == 255 and array_map[x][y][2] == 0:
                goal_x = x
                goal_y = y
                num_of_goals += 1

            # check for red -> 255 0 0 -> robot
            elif array_map[x][y][0] == 255 and array_map[x][y][1] == 0 and array_map[x][y][2] == 0:
                robot_x = x
                robot_y = y
                num_of_robots += 1

            # check for black -> 0 0 0 -> obstacle
            elif array_map[x][y][0] == 0 and array_map[x][y][1] == 0 and array_map[x][y][2] == 0:
                obstacle_arr.append([x,y])


    if num_of_goals != 1:
        print("incorrect number of goals \n", num_of_goals)
    if num_of_robots != 1:
        print("incorrect number of robots \n")
    if num_of_goals == num_of_robots == 1:
        print("set up map correctly \n")

    dictionary = {"data": "" + str(obstacle_arr)}

    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    
    # Writing to sample.json
    with open("your_obstacle.json", "w") as outfile:
        outfile.write(json_object)
    

    # construct command
    exec_string = "python3 A_star_algo/AStar.py"
    # shape of map 
    exec_string += " -c " + str(map_shape[1]) + " -r "+ str(map_shape[0])
    # start point
    exec_string +=  " -s " + str(robot_x) + " -q " + str(robot_y)
    # end point 
    exec_string +=  " -e " + str(goal_x) + " -t " + str(goal_y)
    exec_string += " -l True"

    # print(exec_string)

    # --------------------------------- execute algo ---------------------------------------------------
    subprocess.call(exec_string, shell=True)
    print("executed AStar algorithm \n")
    
    # demo
    # subprocess.call(" python A_star_algo/AStar.py -c 25 -r 25 -s 1 -q 3 -e 23 -t 21 -l True", shell=True)


    # ------------------------ transform output into robot movements ------------------------------------

    # wait until output file is there
    path_file = 'found_path.csv'
    
    while not os.path.exists(path_file):
        time.sleep(0.1)

    if os.path.isfile(path_file):
        # transfer to json
        print('reading file... \n')
        output2commands.csv2json.csv2json(path_file, 'output2commands/position.json')

        # call main.py 
        # subprocess.call('python3 output2commands/main.py', shell=True)
        output2commands.main

            
    else:
        raise ValueError("%s isn't a file!" % path_file)
