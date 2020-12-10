def eight_two(s, n):
    if n > len(s):
        print(s.upper())
    else:
        print(s)
s = str(input("Enter a string: "))
n = int(input("Enter a number of digits: "))
eight_two(s, n)
