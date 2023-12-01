#To find the maximum subarray sum using kadane's algorithm
#Time Complexity: O(N)
#Space Complexity: O(1)

def con_subarr(arr,n):
    MaxSum=arr[0]
    CurrSum=arr[0]
    for i in range(1,n):
        CurrSum+=arr[i]
        if CurrSum < MaxSum:
            CurrSum=0
        else:
            MaxSum=CurrSum
    return (MaxSum)

print(con_subarr([1,-1,2,-5,3,4,5,6,-10],9))