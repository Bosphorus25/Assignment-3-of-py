# Write a function to find the nth Fibonacci number using recursion
def fibo(n):
    if n <= 0:
        return (n)
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n-2)
n = int(input("enter number: "))
print(fibo(n))
        
    
    