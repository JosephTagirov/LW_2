from random import *
L = ['самовар', 'весна', 'лето']
s = choice(L)
b = choice(s)
a = s.index(b)
print(s[0:a] +'?' +s[a+1:len(s)])
print ("Enter a letter")
q = str(input())
if b == q:
    print ("Correct!")
else:
    print ("Wrong!")
