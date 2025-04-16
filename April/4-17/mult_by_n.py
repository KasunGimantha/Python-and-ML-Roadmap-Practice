# Write a function make_multiplier(n) that returns a new function which multiplies any input by n.

def make_multiplier(n):

    def multiplier(y):
        return n*y

    return multiplier


doubler = make_multiplier(2)
tripler = make_multiplier(3)

print(doubler(10))
print(tripler(5))
