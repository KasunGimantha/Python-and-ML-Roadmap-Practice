lst = [4,2,10,9,8,1]
lst2 = [5, 2, 8, 1]
lst3 = [100, 80, 30]
lst4 = [1]


def my_min(lst):
    
    smallest = lst[0]
    
    for x in range(len(lst)):
       if lst[x] < smallest:
           smallest = lst[x]
       
    return smallest  
       
print(my_min(lst))
print(my_min(lst2))
print(my_min(lst3))
print(my_min(lst4))