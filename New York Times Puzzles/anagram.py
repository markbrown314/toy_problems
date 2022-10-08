#!/usr/bin/python3
import itertools
import argparse

def word_lookup(word = "", dictionary = "words.txt", max_len = 10):
    if len(word) > int(max_len):
        raise ValueError("word is too long length: " + str(len(word)) +
                         " > max " + str(max_len))

    with open(str(dictionary), "r") as fp:
        word_set = set(fp.read().splitlines())

    # this has n! growth so 
    r = set()

    for a in itertools.permutations(str(word)):
        s = ''.join(str(e) for e in a)
        r.add(s)
         
    return r & word_set

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('word', type = str, nargs='?', 
                        default = "", help = "input word")
    parser.add_argument('word_list', type = str, nargs='?',
                        default = "words.txt", help = "input text dictionary")
    parser.add_argument('max_len', type = int, nargs='?',
                        default = 10, help ="max length of input string")
    args = parser.parse_args()

    for w in word_lookup(args.word, args.word_list, args.max_len):
        print(w)
