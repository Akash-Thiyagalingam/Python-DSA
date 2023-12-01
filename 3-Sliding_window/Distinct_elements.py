#Time Complexity: O(N)
#Space Complexity: O(1)

#To find Number of distinct characters in k size of sub array
def Distinct_char(arr,k):
    start=0
    end=0
    count=0
    frequency={}
    while(end < len(arr)):
        if (end >= k):
            del frequency[arr[start]]
            arr[start]=count
            if arr[end] not in frequency:
                frequency[arr[end]]=1
                count+=1
            else:
                frequency[arr[end]]+=1
            start+=1
        else:
            if arr[end] not in frequency:
                frequency[arr[end]]=1
                count+=1
            else:
                frequency[arr[end]]+=1
        end+=1
            
    return arr[:(len(arr)-(k-1))]

print(Distinct_char([1,1,2],3))
