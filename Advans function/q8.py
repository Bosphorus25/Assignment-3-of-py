# Create a function to generate a random password of given length, 
# containing uppercase, lowercase, numbers, and special characters.
import random            # random module is used to get sample from mixture 
import string            #string module is used to import all keyboard
print("Hi Generate your Password here")
def hard_passwords():
    length = int(input("Enter length of Password: "))
    all_U = string.ascii_uppercase
    all_L = string.ascii_lowercase              # we store all keyboard numbers alphabet sins in variables
    all_D = string.digits
    all_P = string.punctuation
    mixture = all_U + all_L + all_D + all_P
    x = random.sample(mixture,length)                #it gives samples from mixture of required length
    password = "".join(x)                     # it join all strings into 1
    print(password)
    hard_passwords()
hard_passwords()
