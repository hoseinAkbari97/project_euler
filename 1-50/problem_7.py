def is_prime(num, primes):
    """
    Check if a number is prime using a list of known primes.

    Args:
        num (int): Number to check.
        primes (list): List of previously found prime numbers.

    Returns:
        bool: True if num is prime, False otherwise.
    """
    for p in primes:
        if p * p > num:
            break
        if num % p == 0:
            return False
    return True


def nth_prime(n):
    """
    Find the n-th prime number.

    Args:
        n (int): The position of the prime number to find (1-based index).

    Returns:
        int: The n-th prime number.
    """
    if n == 1:
        return 2

    # List to store found primes
    primes = [2] 
    # Start checking from 3          
    candidate = 3          

    while len(primes) < n:
        if is_prime(candidate, primes):
            primes.append(candidate)
        # Only check odd numbers (even numbers > 2 are not prime)
        candidate += 2     

    return primes[-1]


# Finding the 10001st prime number
n = 10001
print(f"The {n}th prime number is {nth_prime(n)}")
