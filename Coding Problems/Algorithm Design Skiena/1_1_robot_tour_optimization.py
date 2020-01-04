"""
Problem: Robot Tour Optimization
Input: A set S of n points in the plane.
Output: What is the shortest cycle tour that visits each point in set S?
"""
import random
import math
num_points = 3
max_x = 100
max_y = 100
S = set()

def euclidian_distance(a, b):
    if a == b:
        return 0
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def build_adj_matrix(matrix, a, b):
    if matrix == None:
        matrix = {}
    if a in matrix:
        a_dict = matrix[a]
    else:
        matrix[a] = {}
        a_dict = matrix[a]
        a_dict["_closest_point"] = None

    a_dict[b] = euclidian_distance(a,b)

    if a == b:
        return matrix

    if a_dict["_closest_point"] == None:
        a_dict["_closest_point"] = b
        return matrix

    if euclidian_distance(a, a_dict["_closest_point"]) > a_dict[b]:
        a_dict["_closest_point"] = b

    return matrix

def closest_point_adj_matrix(matrix, a):
    if a in matrix:
        a_dict = matrix[a]
    else:
        raise(KeyError("content " + a + " not in adj matrix"))
    return a_dict["_closest_point"]

def lookup_adj_matrix(matrix, a, b):
    if a in matrix:
        a_dict = matrix[a]
    else:
        raise(KeyError("content " + a + " not in adj matrix"))
    
    if b in a_dict:
        raise(KeyError("content " + b + " not mapped to " + a +" in adj matrix"))

    return(a_dict[b])

"""
# generate random set of points
for i in range(0, num_points):
    while True:
        x = random.randint(0,100)
        y = random.randint(0,100)
        if (x,y) not in S:
            break
    S.add((x,y))
"""
S = set([(1,3),(2,7),(3,5)])

matrix = None

# build matrix
for p1 in S:
    for p2 in S:
        matrix = build_adj_matrix(matrix, p1, p2)

print("points", S)
print("adj matrix", matrix)
visited = {}

# build a visit map
for p in S:
    visited[p] = False

visit_count = 1
# get starting point
p = list(S)[0]
visited[p] = True

#while visit_count < len(S):
for p in S:
    print("closest dist for", p, closest_point_adj_matrix(matrix, p))
