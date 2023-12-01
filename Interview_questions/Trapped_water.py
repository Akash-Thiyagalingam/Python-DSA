# To find the total volume of water can stored form the blocks
# The heigth of the blocks are represented in an array
# The complexities of the program given below
# Time complexity : O(N^2)
# Space complexity : O(1)
def trapped_water(arr, n):
    trapped_volume = 0
    if n > 2:
        for each in range(1, n-1):
            min_height = min(max(arr[:each]), max(arr[each+1:]))
            if (min_height - arr[each]) > 0:
                trapped_volume += (min_height - arr[each])
    return trapped_volume

# Optimized way 
# Time complexity : O(N)
# Space complexity : O(N) 
def trapped_rain_water(arr, n):
    trapped_volume = 0
    if n > 2:
        left = [0]*n
        right = [0]*n

        left[0] = arr[0]
        for i in range(n):
            left[i] = max(left[i-1], arr[i])
        
        right[n-1] = arr[n-1]
        for i in range(n-2, -1 ,-1):
            right[i] = max(right[i+1], arr[i])
            
        for each in range(1, n-1):
            min_height = min(left[each-1], right[each+1] )
            if (min_height - arr[each]) > 0:
                trapped_volume += (min_height - arr[each])
        
    return trapped_rain_water