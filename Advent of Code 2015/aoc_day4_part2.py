"""
🎅
--- Part Two ---
Now find one that starts with six zeroes.

Your puzzle answer was 1038736.
"""

import hashlib
import re

def compute_md5sum(input_data):
    #print(input_data)
    md5 = hashlib.md5()
    md5.update(input_data)
    return md5.hexdigest()

input_data = input("input:")
counter = 0
while True:
    test_data = input_data + str(counter)
    hash_digest = compute_md5sum(bytes(test_data, encoding = 'ascii'))
    if re.match("^000000", hash_digest) is not None:
        print("found hash @", hash_digest, "from", test_data)
    counter += 1


