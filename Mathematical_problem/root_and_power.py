# To find the power of a given number
# The program for the power function is given below
# Time complexity : O(m)
# Space complexity : O(1) 
def power(n,m):
    pow_val=1
    for i in range(m):
        pow_val*=n
    return pow_val

# Inorder to reduce the time complexity
# Time complexity : O(logm)
# Space complexity : O(1)
def exponent(n,m):
    ans = 1
    while(m>0):
        if m % 2 == 0:
            n = n * n
            m = m//2
        elif m % 2 == 1:
            ans = n * ans
            m = m - 1
    return ans

# Program to find the root of an given number
# In python we have an operator for finding the power of a number
# We can use the power or exponent operator to finding the root of a number
# The program is given below
# Time complexity : O(1)
# Space complexity : O(1)
def root_by_power(n, m):
    exponent_val = 1 / m
    return (n ** exponent_val)