# To find the given number is prime or not by using recursion 
def isprime(n, i=2):
    if i < 4:
        return True
    elif i == (n//2)+1:
        return True
    elif n%i == 0:
        return False
    else:
        return isprime(n, i+1)


