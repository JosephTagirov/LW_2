N = int(input('How many items will be in the list? '))
L = list();
for i in range(0, N, 1):
    x = int(input('Enter an item '))
    L.append(x)
print(L)
for i in range(N // 2):
    t=L[i]
    L[i] = L[N // 2 + i]
    L[N // 2 + i] = t
print(L)
