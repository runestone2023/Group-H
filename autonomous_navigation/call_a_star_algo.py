import subprocess
import os
import time
import csv
# from PIL import Image
# from numpy import asarray
   


if __name__ == "__main__":
    # read map to pass to the a star algorithm
    # image = Image.open('autonomous_navigation/obstacle_course_images/map_1.png')

    # convert to numpy array for iteration over image
    # numpydata = asarray(image)

    # shape
    # print(numpydata.shape)

    # data
    # print(numpydata)

    # --------------------------------- execute algo ---------------------------------------------------

    subprocess.call(" python A_star_algo\AStar.py -c 25 -r 25 -s 1 -q 3 -e 23 -t 21 -l True", shell=True)


    # ------------------------ transform output into robot movements ------------------------------------

    # wait until output file is there
    path_file = 'found_path.csv'
    
    while not os.path.exists(path_file):
        time.sleep(0.1)

    if os.path.isfile(path_file):
        # read file
        print('reading file... \n')
        with open(path_file, newline='') as csvfile:

            pathreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            count = sum(1 for _ in pathreader)
            print('length is ' + str(count))

            csvfile.seek(0)
            pathreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in pathreader:
                print('x:' + row[0] + ' y:' + row[1])
            
            # transform it into a difference output
    else:
        raise ValueError("%s isn't a file!" % path_file)


