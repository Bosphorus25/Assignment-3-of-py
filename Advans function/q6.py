# Create a function that takes a string and counts the frequency of each character.
def string(x):
    frequency = {}
    for char in x:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
print(string("apple"))
print(string("tfyfgtyftyfyu"))
print(string("trddrokohydfgiokldxtijyftrdtu"))
