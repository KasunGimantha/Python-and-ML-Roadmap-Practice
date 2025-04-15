def multiplier(n):
    def inner(x):
        return x*n
    return inner

double = multiplier(2)
print(double(4))  

triple = multiplier(3)
print(triple(5))