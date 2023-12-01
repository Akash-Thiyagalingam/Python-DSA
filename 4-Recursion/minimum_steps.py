# To find the Minimum number of steps to reach the zero(0)th stair
# By each step we can move one step or equal half of the total numbers of stairs
# Time Complexity: O(2√N)
# Space Complexity: O(1)
def N_to_0(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return (N_to_0(n//2) + 1)
    else:
        return ( N_to_0(n-1) + 1)

print(N_to_0(50))
