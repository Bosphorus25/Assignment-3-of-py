#Write a function that calculates the power of a number without using the ** operator
def power(base,exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result
print(power(4,4))
