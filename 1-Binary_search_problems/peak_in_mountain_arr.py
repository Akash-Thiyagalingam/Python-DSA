# It is otherwise called BITONIC array
def peak_search(arr):
    low=0
    high=len(arr)-1
    while((high-low)>=0):
        mid=(high+low)//2
        if ((mid+1)==len(arr) or (mid-1)==-1) or (arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]):
            return (arr[mid])
        elif(arr[mid-1]>arr[mid]):
            high=mid-1
        elif(arr[mid]<arr[mid+1]):
            low=mid+1
    return -1

print(peak_search([1,2,4,5,4,3,2]))
