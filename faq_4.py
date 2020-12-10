def pairs(L, summ):
    s = set(L)
    edgecase = summ / 2
    if L.count(edgecase) == 2:
        print(edgecase, edgecase)
    s.remove(edgecase)
    for i in s:
        dif = summ - i
        if dif in s:
            print(i, dif)

L = [2, 45, 7, 3, 5, 1, 8, 9]
summ = 10          
pairs(L, summ)
