"""
WIP needs redesign
/r/puzzles/comments/h003pw/again_help_what_is_the_second_word/
"""
import itertools
word_dict = {}

with open("words.txt") as file_input:
    for word in file_input:
        word = word.strip().lower()
        if len(word) == 7:
            if word[0] == 'r' or word[0] == 's' or word[0] == 't':
                # print("input:", word)
                word_dict[word] = True

P1 = ["a", "e", "i", "o", "u"]
P2 = ["r", "s", "t"]
P3 = ["l", "n"]

for p1 in P2:
    for p2 in P1:
        for p3 in P2:
            for p4 in P2:
                for p5 in P3:
                    for p6 in P1:
                        for p7 in P2:
                            word = p1+p2+p3+p4+p5+p6+p7
                            if word in word_dict:
                                print(word)

