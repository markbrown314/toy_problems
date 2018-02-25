import sys
import math

# 1:x1, 2:y1, 3:x2, 4:y2
def distancexy(coord):
    if (len(coord) != 4):
        print("error invalid coordinates")
        sys.exit(0)
    return (math.sqrt((coord[2] - coord[0])**2) + ((coord[3] - coord[1])**2))
