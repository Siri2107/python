# factorial for a number

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*n
        n=n-1
    return fact

print(factorial(n=5))