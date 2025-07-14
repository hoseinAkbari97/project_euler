def sum_square(num):
    """This function calculates the sum of the squares of the
    first n natural numbers which n = num"""
    sum = 0
    for  i in range(1, num+1):
        sum = sum + (i**2)
    return sum

def square_sum(num):
    """This function calculates the square of the sum of the
    first n natural numbers which n = num"""
    sum = 0
    for i in range(1, num+1):
        sum += i
    return (sum**2)

sq_sum = square_sum(100)
sum_sq = sum_square(100)
answer = sq_sum - sum_sq
print(answer)
