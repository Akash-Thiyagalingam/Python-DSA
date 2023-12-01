def floor_search(arr, target):
    low=0
    high=len(arr)-1  
    while((high-low)>=0):
        mid=(high+low)//2
        if ((target==arr[mid])):
            return mid
        elif(target<arr[mid]):
            high=mid-1
        elif(target>arr[mid]):
            low=mid+1
    return arr[low-1] if len(arr)>1 else -1

print(floor_search([2,7], 3))
