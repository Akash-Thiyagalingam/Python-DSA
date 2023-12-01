# To find the no. rotation in an sorted arr
def pivot(arr):
    low=0
    high=len(arr)-1
    while((high-low)>=0):
        mid=(high+low)//2
        if (mid == len(arr)-1) or (arr[mid]>arr[mid+1]): 
            return (mid+1) % len(arr)
        if (mid == 0) or (arr[mid]<arr[mid-1]):
            return mid % len(arr)
        elif(arr[0]>=arr[mid]):
            high=mid-1
        elif(arr[0]<=arr[mid]):
            low=mid+1
    return -1

print(pivot([10,12,13,2,3,4]))