import csv
def load_dictionary(filename):
    l = []
    with open("p022_names.txt", "r") as f:
        inp = csv.reader(f, delimiter=',')
        for item in inp:
            l.extend(item)
    return l

def score_word(word):
    alpha_num = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6,
                 "G":7, "H":8, "I":9, "J":10, "K":11, "L":12,
                 "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18,
                 "S":19, "T":20, "U":21, "V":22, "W":23, "X":24,
                 "Y":25, "Z":26}
    s = 0
    # split word into list of letters
    for i in range(0, len(word)):
        s += alpha_num[word[i]]

    return s

s = 0
for i, word in enumerate(sorted(load_dictionary("p022_names.txt"))):
    s += (score_word(word) * (i+1))

print ("total score:", s)
