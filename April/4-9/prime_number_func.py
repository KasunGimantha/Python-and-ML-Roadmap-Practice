# prime 1-100 with function


def find_prime(n):
    prime_list=[]
    for x in range(2, n):
        is_prime = True
        for y in range(2, int(x**0.5)+1):
            if x % y == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(x)
    return prime_list

print(find_prime(100))