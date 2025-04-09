# Even number sum from 1 to 100 using a loop

newlist = []
for x in range(101):
    if x % 2 == 0:
        newlist.append(x)


print(sum(newlist))
