lst = [1, 4, 8, 2, 9]
lst2 = [100, 55, 1]
lst3 = [2]


def my_max(lst):
    largest = lst[0]

    for x in range(len(lst)):
        if largest < lst[x] :
           largest =  lst[x]
    return largest


print(my_max(lst))
print(my_max(lst2))
print(my_max(lst3))
