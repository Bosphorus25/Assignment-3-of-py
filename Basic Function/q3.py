# Write a function to find the factorial of a number using recursion.
def facatorial(value):
    if value == 1:
        return 1
    else:
        return value * facatorial(value - 1)

print(facatorial(5))
