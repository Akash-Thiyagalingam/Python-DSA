def Binary_search(arr, low, high, target): 
    if(arr[0]<arr[-1]): 
        while((high-low)>=0):
            mid=(high+low)//2
            if ((target==arr[mid])):
                return (mid)
            elif(target<arr[mid]):
                high=mid-1
            elif(target>arr[mid]):
                low=mid+1
    else:
        while((high-low)>=0):
            mid=(high+low)//2
            if ((target==arr[mid])):
                return (mid)
            elif(target>arr[mid]):
                high=mid-1
            elif(target<arr[mid]):
                low=mid+1
    return -1 if arr[-1]!=target else len(arr)-1

def peak_search(arr):
    low=0
    high=len(arr)-1
    while((high-low)>=0):
        mid=(high+low)//2
        if ((mid+1)==len(arr) or (mid-1)==-1) or (arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]):
            return (mid)
        elif(arr[mid-1]>arr[mid]):
            high=mid-1
        elif(arr[mid]<arr[mid+1]):
            low=mid+1
    return -1

def find_element(arr, target):
    peak=peak_search(arr)
    search=Binary_search(arr, 0, peak, target)
    if search==-1:
        search=Binary_search(arr, peak, len(arr)-1, target)
    return search

print(find_element([3,5,7,6,4],4))