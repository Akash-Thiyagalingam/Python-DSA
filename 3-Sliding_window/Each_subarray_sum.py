#To find sum of each subarray of size k
#Time Complexity: O(N)
#Space Complexity: O(1)
def sum_of_subarray(n,arr,k): 
    if k>n:
        k=n
    output=[]
    rem_el=0
    sum_el=arr[0]
    for i in range(1,k):
            sum_el+=arr[i]
            
    for i in range(k,n):
        output+=[sum_el]
        sum_el=(sum_el-arr[rem_el])+arr[i]
        rem_el+=1
    return output

print(sum_of_subarray(6,[1,2,3,4,5,6],3))