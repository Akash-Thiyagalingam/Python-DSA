#Binary search ,Finding pair of numbers == sum
def search(arr, low, high, remain):  
    while((high-low)>=0):
        mid=(high+low)//2
        if ((remain==arr[mid])):
            return (mid)
        elif(remain<arr[mid]):
            high=mid-1
        elif(remain>arr[mid]):
            low=mid+1
    return -1

#It has time complesity O(n*longn)
def find_sum_pair(arr,size,n): 
    index=[None,None]
    length=size-1 
    for i in range(size):
        second=search(arr, i+1, length, n-arr[i] )
        if second!=-1:
            index[0]=i
            index[1]=second
            break
    return index


print(find_sum_pair([1,2,3,4,5,7],6,10))