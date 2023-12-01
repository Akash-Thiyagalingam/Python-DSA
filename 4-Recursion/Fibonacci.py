# In Fibonacci series finding Nth term using recursion
# Time complexity : O(N!)
# Space complexity : O(1)
def FiboRecur(n):
    if n == 0 or n == 1:
        return n
    else:
        return (FiboRecur(n-1) + FiboRecur(n-2))