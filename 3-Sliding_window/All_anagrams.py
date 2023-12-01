#Time Complexity: O(N)
#Space Complexity: O(1)

#Find all the anagram an string with the k string
#Ex : Input 'akakakaka','aka'  Output : 4
def All_Anagram(arr,k):
    start=0
    k_fre={}
    SubArr_fre={}
    anagram_count=0  
    for end in range(len(arr)):
        if end >= len(k) : 
            #This is for finding the frequency of Subarrays by Sliding Window technique 
            if SubArr_fre[arr[start]] == 1 :
                del SubArr_fre[arr[start]]
            else:
                SubArr_fre[arr[start]]-=1
            if arr[end] not in SubArr_fre :
                SubArr_fre[arr[end]]=1
            else:
                SubArr_fre[arr[end]]+=1
            start+=1

        else:
            #This is for finding the ferquency of first len(k) of characters in both k and arr strings
            if k[end] not in k_fre :
                k_fre[k[end]]=1
            else:
                k_fre[k[end]]+=1
            if arr[end] not in SubArr_fre :
                SubArr_fre[arr[end]]=1
            else:
                SubArr_fre[arr[end]]+=1

        #This condition for checking the frequency of chcaracters of both string
        if end >= len(k)-1:
            if SubArr_fre == k_fre :
                anagram_count+=1
       
    return anagram_count


print(All_Anagram('akakakaka','akk'))