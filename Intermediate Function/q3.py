#  Write a function to check whether a string is a palindrome
def palindrome():
    num = input("enter a value: ")
    num1 = (num[ : :-1])
    if num == num1:
        print(num,"is palindrome")
    else:
        print(num,"is not palindrome")
palindrome()
palindrome()
palindrome()