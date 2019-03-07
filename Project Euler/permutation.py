# provide all permutations of a string
def permute(rem, fixed = ""):
    if len(rem) == 1:
        yield(fixed + rem)
    for i in range(0, len(rem)):
        for string in permute(rem[:i] + rem[i+1:], fixed + rem[i]):
            yield string
    
if __name__ == "__main__":
    for i, string in enumerate(permute("abc")):
        print(i+1, string)