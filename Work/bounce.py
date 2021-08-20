# bounce.py
#
# Exercise 1.5
height = 100
cut = 0.6
i = 1

while i <= 10:
    height *= cut
    print(i, round(height, 4))
    i+=1



