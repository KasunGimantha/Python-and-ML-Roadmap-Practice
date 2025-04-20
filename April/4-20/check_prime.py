def is_prime(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 2:
        raise ValueError("No primes below 2")
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(1))
