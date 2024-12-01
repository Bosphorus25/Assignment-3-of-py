# Create a function that accepts a dictionary and returns the key with the highest value.
def high_value():
    all_values = {
        "apple" : 4,
        "orange" : 7,
        "banana" : 3,
        "grapes" : 12,
        "mellon" : 1
    }
    high = max(all_values,key = all_values.get)
    print(high)
high_value()
