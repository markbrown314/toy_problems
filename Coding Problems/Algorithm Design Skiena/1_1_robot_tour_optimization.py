"""
Problem: Robot Tour Optimization
Input: A set S of n points in the plane.
Output: What is the shortest cycle tour that visits each point in set S?
"""
import random
import math
num_points = 10
max_x = 100
max_y = 100
S = set()

def euclidian_distance(a, b):
    if a == b:
        return 0
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def build_adj_list(adj_list, a, b):
    if adj_list == None:
        adj_list = {}
    if a in adj_list:
        a_dict = adj_list[a]
    else:
        adj_list[a] = {}
        a_dict = adj_list[a]

    a_dict[b] = euclidian_distance(a,b)

    return adj_list

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
"""

adj_list = None

# build adjacency list
for p1 in S:
    for p2 in S:
        adj_list = build_adj_list(adj_list, p1, p2)

print("points", S)
print("adjacency list", adj_list)
visited = {}
tour = []

# build a visit map
for p in S:
    visited[p] = False

visit_count = 1
# get starting point
p = list(S)[0]
visited[p] = True

while True:
    print(p, end="")
    if visit_count >= len(S):
        break
    print(" -> ", end="")
    # sort adjacency list
    path = []
    v = adj_list[p]
    for key in v:
        path.append([key, v[key]])
    sorted(path, key = lambda p: p[1])
    for neighb in path:
        np = None
        #print (neighb[0], visited[neighb[0]])
        if not visited[neighb[0]]:
            np = neighb[0]
            break
    if not np:
        raise(LookupError("Cannot find unvisited neighbor!"))
    visited[np] = True
    p = np
    visit_count += 1    