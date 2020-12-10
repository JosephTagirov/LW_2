L = [3, 6, 7, 4, -5, 4, 3, -1]
if sum(L) > 2:
    print (len(L))
    a = max(L)
    b = min(L)
if abs(a-b) >= 10:
     L.sort()
     print (L)
else:
    print("The difference is less than 10")
