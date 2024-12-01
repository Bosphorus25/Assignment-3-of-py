# Create a function to check if a given number is prime.
def prime_num(num):
    if num <= 1:
        print(num,"not a prime number")
    elif num > 1:
        for i in range(2,num):
            if num % i == 0:
                print("not a prime number")
                break
        else:
            print("its a prime number")
    return num
print(prime_num(18))