# ⚔️ Challenge 2: Higher-Order Functions
# Write a function:
# def apply_twice(func, value):
# It should:
# Take a function (func) and a value (value)
# Apply func to the value two times
# → Meaning: return func(func(value))
def add_three(x):
    return x+3

def apply_twice(func,value):
    
    return func(func(value))

    
print(apply_twice(add_three,7))    

def square(x): return x * x 
 
print(apply_twice(square, 2))  