# Create a function that takes a list of integers and returns the sum of all even numbers
def sum_of_even(numbers):
    sum = 0
    for i in numbers:
        if i % 2 == 0:
            sum += i
    return sum
print(sum_of_even([2,3,7,6]))

