# Create a function to check if two strings are anagrams
def anagram(stng1,stng2):
    if sorted(stng1) == sorted(stng2):
        print("yes the strings are anagram")
    else:
        print("the strings is not anagram")
anagram(("qazmpl"),("mqupzl"))
anagram(("listen"),("silent"))
anagram(("triangle"),("integral"))