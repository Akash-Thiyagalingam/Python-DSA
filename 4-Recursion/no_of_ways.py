# To find the total number of ways to claimb the n of stairs with only the number steps can be used claimx
# The steps are represented in an array of steps 
def noOFways(n, arr):
    if n == 0:
        return 1
    ways = 0
    for steps in arr:
        if n-steps >= 0:
            ways += noOFways(n-steps, arr)
    return ways

print(noOFways(10,[2, 4, 5, 8]))
