# use caching
global path_map

def lookup_path(x, y):
    global path_map
    key = str(x)+","+str(y)
    if key in path_map:
            return path_map[key]

    path_map[key] = search_path(x,y)
    return path_map[key]

def search_path(x, y):
    print(x,y)
    if x == 0 or y == 0:
        print(1)
        return 1

    return lookup_path(x - 1, y) + lookup_path(x, y - 1)

# start
path_map = {}
print("result:", search_path(20, 20))
