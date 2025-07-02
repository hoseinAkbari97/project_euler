def biggest_prime_factor(n):
    factor = 2
    last_factor = 1
    while n > 1:
        if n % factor == 0:
            last_factor = factor
            n = n // factor
            while n % factor == 0:
                n = n // factor
        factor += 1
        if factor * factor > n:
            if n > 1:
                last_factor = n
                break
    return last_factor

print(biggest_prime_factor(600851475143))
