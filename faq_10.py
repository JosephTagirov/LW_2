def ext(seq):
    ss = set()
    ss1 = ss.add
    return [x for x in sq if not (x in ss or ss1(x))]
sq = [1, 4, 4, 5, 7, 99, 99, 4, 1, 5]
print(ext(sq))
