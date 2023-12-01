#To find the total number of consiguitive 1's for an array we can flip k number of 0s 
#Time Complexity: O(N)
#Space Complexity: O(1)

def longest_1s(arr,k):
    zeros=0
    start=0
    CurrCount=0
    TotCount=0
    for i in arr:
        if i==0 :
            zeros+=1
        if zeros == (k+1):
            zeros-=1
            CurrCount=zeros
        CurrCount+=1
        TotCount=max(TotCount,CurrCount)

    return TotCount

print(longest_1s([1,1,0,1,0,1,0,1,1,1,0,0,0,0],3))
