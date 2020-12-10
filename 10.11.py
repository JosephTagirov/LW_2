from random import *
N = 3
M = 3
lst = [[randint(1, 9) for i in range(N)] for i in range(M)]
for i in lst:
    print()
    for j in i:
        print (j, end = " ")
