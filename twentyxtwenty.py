import math
import re

MAX_X = 20
MAX_Y = 20

def map_file_to_20x20_array(file_name):
        regex = re.compile('[0-9]')
        array = [[0] * MAX_X] * MAX_Y
        with open(file_name, 'r') as f:
            input_data = f.read()

        # remove white space and store two digit number
        pos = 0
        num = ""
        for i in range(0, len(input_data)):
            if regex.match(input_data[i]):
                num += str(input_data[i])
                x = pos % MAX_X
                y = int(pos / MAX_Y)

                if len(num) >= 2:
                    if y >= MAX_Y:
                        raise IndexError('too many values in input file')

                    array[x][y] = int(num)

                    num = ""
                    pos += 1

        print("x",x,"y",y)
        if x != (MAX_X - 1) or y != (MAX_Y - 1):
            raise IndexError('too few values in input file')

        return array

def pretty_print_20x20(array):
    for i in range(0, len(array)):
        x = i % MAX_X
        y = int(i / MAX_Y)
        if x == 0 and y != 0:
            print("")
        print("%02d" %array[x][y], end = '')
