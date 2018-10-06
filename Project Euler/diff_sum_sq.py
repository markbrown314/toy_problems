from functools import reduce
def sq_sum(num_list):
    square_list = list(map(lambda x:x**2, num_list))
    sum = reduce((lambda x,y:x + y), square_list)
    return sum

def sum_sq(num_list):
    sum = reduce((lambda x,y:x + y), num_list)
    sum = sum**2
    return sum

def sum_sq_difference(x):
    num_list = list(range(1, x+1))
    sum1 = sum_sq(num_list)
    sum2 = sq_sum(num_list)
    return sum1 - sum2
