#pair_sum for one array
def pair_sum(arr,val):
    start=0
    end=len(arr)-1
    pairs=set()
    while (start<end):
        if (arr[start]+arr[end])==val :
            pairs.add((start, end)) # I dont know why the set.add function performs like this
            pairs.add((arr[start], arr[end]))
            start+=1
            end-=1
        elif((arr[start]+arr[end])>val):
            end-=1
        else:
            start+=1
    return pairs

print(pair_sum([1,2,3,4,6,8,9,11,13,15,19],16))

#Another method
def sum_pair(arr,val):
    seen=set()
    output=set()
    for i in arr:
        target=val-i
        if target not in seen:
            seen.add(i)
        else:
            output.add((min(i,target),max(i,target)))
    return output

print(sum_pair([1,2,3,4,6,8,9,11,13,15,19],16))
        
