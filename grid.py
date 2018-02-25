import math
import re
import sys

class Grid:

    def __init__(self, file_name, max_x, max_y, num_len):
        self.array = None
        self.file_name = file_name
        self.max_x = max_x
        self.max_y = max_y
        self.num_len = num_len
        self.map_file()

    def map_file(self):
            self.array = [[0 for y in range(self.max_y)] for x in range(self.max_x)]
            regex = re.compile('[0-9]')

            with open(self.file_name, 'r') as f:
                input_data = f.read()

            # remove white space and store two digit number
            pos = 0
            num = ""
            for i in range(0, len(input_data)):
                if regex.match(input_data[i]):
                    num += str(input_data[i])
                    x = pos % self.max_x
                    y = int(pos / self.max_x)

                    if len(num) >= self.num_len:
                        if y >= self.max_y:
                            raise IndexError('too many values in input file')

                        #print("pos", pos, "x", x, "y", y, "num", num, file=sys.stderr)
                        self.array[x][y] = int(num)
                        num = ""
                        pos += 1

            if x != (self.max_x - 1) or y != (self.max_y - 1):
                #print("x", x, "y", y, "num_len", "max_x", self.max_x, "max_y", self.max_y, self.num_len, file=sys.stderr)
                raise IndexError('too few values in input file')

            return self.array

    def pretty_print(self):
        if self.array is not None:
            for i in range(0, self.max_x * self.max_y):
                x = i % self.max_x
                y = int(i/self.max_x)
                if x == 0:
                    print("")
                print_format = " %0" + str(self.num_len) + "d "
                print(print_format %self.array[x][y], end='')
            print("")

    def select_items(self, offsets, coordinates):
        x = coordinates[0]
        y = coordinates[1]
        items = []
        if self.array is not None:
            for offset in offsets:
                opx = offset[0]
                opy = offset[1]
                if x + opx < self.max_x:
                    if y + opy < self.max_y:
                        #print("*x", x + opx, "*y", y + opy)
                        yield self.array[x + opx][y + opy]
