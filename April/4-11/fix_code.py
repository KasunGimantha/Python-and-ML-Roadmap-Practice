# def greet(name):
#     print("Hello " + name)
#     return

# greet()  # <- Fix this. Do NOT patch with a random string. Explain WHY this breaks.


# def greet(name):
#     print("Hello " + name)
#     return

# greet()  # <- Fix this. Do NOT patch with a random string. Explain WHY this breaks.

#the code break becuase we are not passing any value to greet() function.so greet function pass empty value while it expect value for name argument.when printing inside greet(),there is no value assigned for name so TypError error occure
#fixed code:
def greet(name):
    print("Hello " + name)
    return

greet("kasun") #  passing value into parameter