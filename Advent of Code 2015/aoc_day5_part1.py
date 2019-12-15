"""
🎅
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or 
aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the
 other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double 
letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the 
letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?
"""

puzzle_input = "ugknbfddgicrmopn"
prev_state = "+"
vowel_count = 0
vowel_set = {'a','e','i','o','u'}
naughty_set = {'ab','cd','pq','xy'}
dupe_found = False

for state in puzzle_input:

    check_state = prev_state + state
    # ab, cd, pq, or xy
    if check_state in naughty_set:
        print("naughty!")
        exit(0)

    if prev_state == state:
        dupe_found = True

    if state in vowel_set:
        vowel_count += 1
if not dupe_found and vowel_count < 3:
    print("naughty!")
else:
    print("nice!")

