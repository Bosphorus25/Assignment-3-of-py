# Write a function to count the vowels in a given string
def total_vowels(x):
    count = 0
    vowels = ("a,e,i,o,u")
    for char in x:
        if char in vowels:
            count+= 1
    return count
print(total_vowels("tdfyuguihou"))
