def ceiling_search(arr, target):
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
    return arr[low]

print(ceiling_search([1,2,3,7], 5))
