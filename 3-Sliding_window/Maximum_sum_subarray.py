#To find the maximum sum of the each subarray of size k
#Time Complexity: O(N)
#Space Complexity: O(1)

def max_sum_sub(arr,n,k):
    MaxSum=arr[0]
    SubSum=arr[0]
    start=0
    for end in range(1,n):
        if (end>k-1):
            SubSum=(SubSum-arr[start])+arr[end]
            MaxSum=max(MaxSum,SubSum)
            start+=1
        else:
            SubSum+=arr[end]
    return MaxSum

print(max_sum_sub([1,2,3,4,5,6,7],7,3))
        