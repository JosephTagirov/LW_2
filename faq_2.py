mass = [i for i in range(10)]
mass.append(8)

mass.sort()
for i in range(len(mass) - 1):
    if mass[i] == mass[i + 1]:
        print(mass[i])
