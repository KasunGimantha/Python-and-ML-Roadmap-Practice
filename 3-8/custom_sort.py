
# declare tuples

mytuple1 = (23, 54)
mytuple2 = (65, 89)
mytuple3 = (67, 29)
mytuple4 = (98, 45)

#putting tuples into a list

mylist = [mytuple1, mytuple2, mytuple3, mytuple4]

#declaring sorting function
def sort_tuple(mylist):
    mylist.sort(key=lambda x: x[1])
    print(mylist)

sort_tuple(mylist)
