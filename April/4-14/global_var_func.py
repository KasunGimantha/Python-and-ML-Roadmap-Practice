#A function that modifies a global variable from inside.
global global_var

def global_func():
    global global_var
    global_var = 2
    return global_var

global_var = 6
print(global_var)
print(global_func())