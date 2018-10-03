def permute(a, b):
    if len(b) == 1:
        yield(a+b)
    for i in range(0, len(b)):
        for j in permute(a + b[i], b[:i] + b[i+1:]):
            yield j

if __name__ == "__main__":
    for i in permute("", "abcd"):
        print(i)