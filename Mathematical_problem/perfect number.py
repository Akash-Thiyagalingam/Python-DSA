# Perfect number is a numer which is equal to it's sum of the factors
def perfect_no (n):
    total = 0
    if n == 1 :
        total = 1
    for divisor in range(1, n):
        if n % divisor == 0:
            total += divisor
    if total == n:
        return ("It is a prime number")
    else :
        return ("It is not a prime number")
    
