#function that nests another function and uses nonlocal to change a variable from the outer function.

def outer_func(): #call outer function
    msg = 'original' 
    def nested_func(): #call nested function
        nonlocal msg   #declare msg as nonlocal
        msg = 'altered' #assign new value
        return msg  #return msg from nested function
    nested_func() #call nested function inside outer function
    return msg  #return msg from outer function

print(outer_func())    