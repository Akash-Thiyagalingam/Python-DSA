# Smallest subarray which has sum <= k , In this we can use sorting algorithm.
# This is brute force approach solution.
# Time complexity => O(n**2)
# Space complexity => O(1)
def SmallSubSum(arr,k):
    minlength=len(arr)
    for i in range(len(arr)-1):
        currsum=0
        for j in range(i,len(arr)): 
            currsum+=arr[j]
            if (currsum >= k):
                minlength=min(minlength, (j-i)+1)
                break
    return minlength if minlength != len(arr) else 0

print(SmallSubSum([1,2,3,5],6))

#By using sliding window with two pointers
def SmallSubSum_sli_win(arr,k):
    st=0
    end=0
    minlength=len(arr)
    sum=0
    while (end<len(arr)):
        sum+=arr[end]
        while(sum >= k and st<=end):
            minlength=min (minlength, sum)
            sum=sum-arr[st]
    return minlength if minlength != len(arr) else 0

print(SmallSubSum([1,2,3,5],6))
