# In Fibonacci series finding Nth term using recursion
# Time complexity : O(N!)
# Space complexity : O(1)
def FiboRecur(n):
    if n == 0 or n == 1:
        return n
    else:
        return (FiboRecur(n-1) + FiboRecur(n-2))


# In Fibonacci series finding Nth term by the elements adding in the list
# By this we can get the whole fibonacci series in a list
# Time Complexity : O(N)
# Space Complexity : O(N)
def FiboList(n):
    fiboSeries = [0,1]
    for i in range(2,n+1):
        fiboSeries.append(fiboSeries[i-1] + fiboSeries[i-2])
    return fiboSeries[n]



 # In Fibonacci series finding Nth term by the two variables
# Time Complexity : O(N)
# Space Complexity : O(1)
def Fibo(n):
    first = 0
    second = 1
    if n == 1:
        return first
    elif n == 2:
        return second
    else:
        for i in range(2, n+1):
            third = first + second
            first = second
            second = third
    return third



# Finding fibonacci term by using formula
# It not produce the occurate result, if th n < 71 
# Time Complexity : O(1)
# Space Complexity : O(1)
import math
def FiboFor(n):
    root_5 = math.sqrt(5)
    return int((((root_5 + 1)/2) ** n) /root_5)