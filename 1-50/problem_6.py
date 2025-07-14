def compute_difference(n):
    """
    Computes the difference between the square of the sum and the sum of the squares
    of the first n natural numbers using mathematical formulas.
    
    Args:
        n (int): The number of natural numbers to consider
        
    Returns:
        int: The difference (square of sum) - (sum of squares)
    """
    # Calculate sum of squares using formula:
    # sum_sq = 1² + 2² + ... + n² = n(n+1)(2n+1)/6
    sum_sq = n * (n + 1) * (2 * n + 1) // 6
    
    # Calculate square of sum using formula:
    # square_sum = (1 + 2 + ... + n)² = [n(n+1)/2]²
    square_sum = (n * (n + 1) // 2) ** 2
    
    # Return the difference: (square of sum) - (sum of squares)
    return square_sum - sum_sq

# Compute and print result for n=100
print(compute_difference(100))
