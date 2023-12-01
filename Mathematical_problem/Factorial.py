# Factorial of a number using recursion 
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return(fact(n-1) * n)

# Factorial of a number without recursion
def factorial(n):
    mul = 1
    for i in range(2,n+1):
        mul *= i
    return mul
