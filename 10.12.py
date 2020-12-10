from random import *
N = 3
M = 5
lst = [[randint(1, 9) for i in range(N)] for i in range(M)]
for i in lst:
    print()
for j in i:
    print (j, end = " ")
    c = 0
    ind = 0
for i in range(N):
    for j in range(i):
        cnt = lst[i].count(lst [i] [j])
        if cnt > c:
            ct = cnt
            intt = i
            print()
print (cnt)
print (intt+1)
