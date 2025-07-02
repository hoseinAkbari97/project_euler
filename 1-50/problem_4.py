def is_palindromic(number):

    list = []

    while True:
        if number < 10:
            list.insert(0, int(number))
            return list
        else:
            rem = int(number % 10)
            list.insert(0, rem)
            number = number/10

input = 1000
print(is_palindromic(input))
            