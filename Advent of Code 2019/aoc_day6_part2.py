"""
🎅
--- Part Two ---
Now, you just need to figure out how many orbital transfers you (YOU) need to take to get to
Santa (SAN).

You start at the object YOU are orbiting; your destination is the object SAN is orbiting. An orbital
transfer lets you move from any object to an object orbiting or orbited by that object.

For example, suppose you have the following map:

COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
Visually, the above map of orbits looks like this:

                          YOU
                         /
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
In this example, YOU are in orbit around K, and SAN is in orbit around I. To move from K to I, a
minimum of 4 orbital transfers are required:

K to J
J to E
E to D
D to I
Afterward, the map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
                 \
                  YOU
What is the minimum number of orbital transfers required to move from the object YOU are orbiting
to the object SAN is orbiting? (Between the objects they are orbiting - not between YOU and SAN.)
"""
puzzle_input = ""
input_data = ""
"""
with open("aoc_day6_input_data.txt") as input_file:
    for line in input_file:
        puzzle_input += line
"""
puzzle_input = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
"""

orbit_map = {}
child_map = {}
parent_map = {}
visit_map = {}
orbit_stack = []
transfers = 0

for input_data in puzzle_input.split("\n"):
    if input_data.find(")") < 1:
        continue
    sobject = input_data.split(")")
    if len(sobject) != 2:
        continue
    orbit_map[sobject[1]] = sobject[0] # B)A, A->B
    visit_map[sobject[0]] = 0
    visit_map[sobject[1]] = 0

    if sobject[0] in child_map:
        child_map[sobject[0]].append(sobject[1]) 
    else:
        child_map[sobject[0]] = [sobject[1]]

    parent_map[sobject[0]] = sobject[1]

print("child", child_map)
print("parent", parent_map)
cur = parent_map["YOU"]
while True:
    if cur == "SAN":
        print("transfer count:", transfers-2)
        break

    node_count = len(child_map[cur])
    i = visit_map[cur]

    # go up to the parent
    if i >= node_count:
        cur = orbit_stack.pop()
        transfers -= 1
        continue

    # descend
    if i < node_count:
        orbit_stack.append(cur)
        visit_map[cur] += 1
        print("cur", cur, "visiting:", visit_map[cur])

        if cur not in child_map:
            print ("cur", cur, "i =", i, "(empty)")
            continue
        prev = cur
        cur = child_map[prev][i]
        print (prev, "->", cur, ":", transfers + 1)
        transfers += 1
        continue
    print ("done")
    break