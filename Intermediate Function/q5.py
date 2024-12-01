# Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.
def gcd(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller + 1):
        if ((x % i == 0) and (y %i == 0)):
            gcdis = i
    return gcdis
print(gcd(12,30))

