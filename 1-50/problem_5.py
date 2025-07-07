# Finding the GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Finding the LCM
def lcm(a, b):
    return a * b // gcd(a, b)

result = 1
for i in range(1, 21):
    result = lcm(result, i)

print(result)
