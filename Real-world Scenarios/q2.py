# Create a function to generate a random password of given length, 
# containing uppercase, lowercase, numbers, and special characters.
import random
import string
print("Hi Generate your Password here")
def hard_passwords():
    length = int(input("Enter length of Password: "))
    all_U = string.ascii_uppercase
    all_L = string.ascii_lowercase
    all_D = string.digits
    all_P = string.punctuation
    mixture = all_U + all_L + all_D + all_P
    x = random.sample(mixture,length)
    password = "".join(x)
    print(password)
    hard_passwords()
hard_passwords()
