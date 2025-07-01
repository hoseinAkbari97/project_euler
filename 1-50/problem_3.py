def calculate_factors(number):
    
    """This function calculates the factors
    of the given number"""
    factors = []
    for i in range(2, number/2):
        if number % i == 0:
            factors.append(i)
            
    return factors

def calculate_prime_factors(factors):
    
    """This function calculates the prime elements 
    of the given list"""


def biggest_prime_factor(number):
    
    """This function calculates the biggest
    prime factor of the given number"""
    factors = calculate_factors(number)  
    
    prime_factors = calculate_prime_factors(factors)
    