a = [1, 2, 3, 4, 5, 6, 4, 4, 5]
b = [item for item in set(a) if a.count(item) > 1]
print(b)
