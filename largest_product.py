import io
import re

def map_file_to_array(file_name):
        regex = re.compile('[0-9]')
        array = []
        with open(file_name, 'r') as f:
            input_data = f.read()
        # remove white space
        for i in range(0, len(input_data)):
            if regex.match(input_data[i]):
                array.append(input_data[i])
        return array

def largest_product(series, file_name):
    input_list = map_file_to_array(file_name)
    output_list = []
    input_len = len(input_list)

    if not series:
        return

    for i in range(0, len(input_list)):
        product = int(input_list[i])
        for j in range (i + 1, i + series):
            if (j >= input_len):
                break
            product = product * int(input_list[j])
        output_list.append(product)

    print(list(reversed(sorted(output_list))))
