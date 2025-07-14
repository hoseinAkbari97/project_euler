def sum_square(num):
    """This function calculates the sum of the squares of the
    first n natural numbers which n = num"""
    sum = 0
    for  i in range(1, num+1):
        sum = sum + (i**2)
    return sum



print(sum_square(10))
