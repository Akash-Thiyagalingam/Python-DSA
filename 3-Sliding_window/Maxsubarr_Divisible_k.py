# Maximum length subarray of an array with the sum divisible by k
# We have to implement it on Brute force 
#Time complexity : O(N**3)
def subarray_divisible_k_BF(arr,k):
    length=0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum = 0
            for l in range(i,j+1):
                sum+=arr[l]
            if (sum % k == 0):
                length=length if length > j-i+1 else j-i+1
    return length 

print(subarray_divisible_k_BF([1,7,6,1,4,6],3))


# Simple optimization to reduce the complexity
# Time complexity : O(N**2) 
def subarray_divisible_k(arr,k):
    length=0
    for i in range(len(arr)):
        cur_sum=0
        for j in range(i,len(arr)):
            cur_sum+=arr[j]
            if (cur_sum % k == 0):
                length=length if length > j-i+1 else j-i+1
    return length 

print(subarray_divisible_k([2,7,6,1,4,4],3))

# We can implement this using hashmap or dictionary in python
# It has linear time complexity, Its Time Complexity : O(N) 
def subarray_divisible_k_map(arr,k):
    map_rem={}
    cur_sum=0
    mx = 0
    for i in range(len(arr)):
        cur_sum+=arr[i]
        rem = cur_sum % k
        if rem == 0:
            mx=mx if mx > i+1 else i+1
        if rem < 0:
            rem += k
        if rem not in map_rem:
            map_rem[rem] = i
        else:
            length = i- map_rem[rem]
            mx = mx if mx > length else length

    return mx

print(subarray_divisible_k_map([2,7,6,1,4,4],3))
            