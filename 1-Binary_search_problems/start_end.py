def search(arr, low, high, val, front):  
    while((high-low)>=0):
        mid=(high+low)//2
        if ((val==arr[mid])):
            if (front):
                if (mid-1)==-1 or (arr[mid]>arr[mid-1]):
                    return mid
                else:
                    high=mid
            else:
                if (mid +1)==len(arr) or (arr[mid]<arr[mid+1]):
                    return mid
                else:
                    low=mid+1
        elif(val<arr[mid]):
            high=mid
        elif(val>arr[mid]):
            low=mid+1
    return -1


def occur_range(arr,val):
    index=[-1,-1]
    index[0]=search(arr, 0, len(arr)-1, val, True)    
    if index[0]!=-1:
        index[1]=search(arr, 0, len(arr)-1, val, False)
    return index

print(occur_range([4,4,4],4))
