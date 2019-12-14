"""
🎅
--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts
for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least
five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given
below) followed by a number in decimal. To mine AdventCoins, you must find Santa the
lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of
abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest
such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash
starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks
like 000006136ef....

Your puzzle answer was 254575.
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
    if re.match("^00000", hash_digest) is not None:
        print("found hash @", hash_digest, "from", test_data)
    counter += 1


