# prime 1-100
for x in range(2, 100):
    is_prime = True
    for y in range(2, int(x**0.5)+1):
        if x % y == 0:
            is_prime = False
            break
    if is_prime:
        print(x)
