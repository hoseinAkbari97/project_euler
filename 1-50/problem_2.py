def fibo_calculator(number):
    """Calculate the nth fibo number for n = number"""
    
    if number == 1:
        return 1
    
    elif number ==2:
        return 2
    
    else:
        return fibo_calculator(number-1) + fibo_calculator(number-2)
    
sum = 0
iter = 1
while True:
    fibo = fibo_calculator(iter)
    iter += 1
    if fibo > 4000000:
        break
    elif fibo % 2 ==1:
        continue
    else:
        sum += fibo
    

print(sum)
    