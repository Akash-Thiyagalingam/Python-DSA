def Binary_search(arr, low, high, target): 
     
    while((high-low)>=0):
        mid=(high+low)//2
        if ((target==arr[mid])):
            return (mid)
        elif(target<arr[mid]):
            high=mid-1
        elif(target>arr[mid]):
            low=mid+1
    return -1

def pivot(arr):
    low=0
    high=len(arr)-1
    while((high-low)>=0):
        mid=(high+low)//2
        if (mid == len(arr)-1) or (arr[mid]>arr[mid+1]): 
            return mid % len(arr)
        if (mid == 0) or (arr[mid]<arr[mid-1]):
            return mid-1 % len(arr)
        elif(arr[0]>=arr[mid]):
            high=mid-1
        elif(arr[0]<=arr[mid]):
            low=mid+1
    return -1

def find_element(nums, target):
    peak=pivot(nums)
    if (nums[peak]==target):
        return peak
    search=Binary_search(nums, 0, peak-1, target)
    if search==-1:
        search=Binary_search(nums, peak+1, len(nums)-1, target)
    return search

print(find_element([10,1,3,4,5],4))