import subprocess
# from PIL import Image
# from numpy import asarray


# read map to pass to the a star algorithm
# image = Image.open('autonomous_navigation/obstacle_course_images/map_1.png')

# convert to numpy array for iteration over image
# numpydata = asarray(image)

# shape
# print(numpydata.shape)

# data
# print(numpydata)

subprocess.call(" python Implementation-of-A-Algorithm-Visualization-via-Pyp5js-\AStar.py -c 25 -r 25 -s 1 -q 3 -e 23 -t 21 -l True", shell=True)