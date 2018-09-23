from itertools import permutations
import numpy as np

for x in permutations('123456789', 6):
    x_int = int(''.join(x))
    found = True
    a = np.array(x)

    for mul in range(2,7):
        a = np.vstack((a, tuple(str(x_int * mul))))

    for row in range(0,6):
        if np.unique(a[row]).size != 6:
            found = False
            break

    if found:
        for col in range(0,6):
            if np.unique(a[:,[col]]).size != 6:
                found = False

    if found:
        print(a)
        break
