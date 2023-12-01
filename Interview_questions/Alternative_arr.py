# To alternate the given sorted array in max and min order
# Sample :
#   input : [1,2,3,4,5,6]
#   output : [6,1,5,2,3,4]
# The program for the given problem is given below
# Time complexity : O(n)
# Space complexity : O(n/2)

def alter_arr(arr, n):
    less_val = arr[: n//2]
    mid = arr[len(arr) //2]
    index = -1
    for i in range(0, n, 2):
        arr[i] = arr[index]
        index -= 1

    if n % 2 == 1 :
        arr[n-1] = mid  
    else :
        arr[n-2] = mid

    index = 0
    for i in range(1, n, 2):
        arr[i] = less_val[index]
        index += 1
    
# To reduce the space complexity, the solution given can be used
# Time complexity : O(n)
# Space complexity : O(1)
def rearrange(arr, n):
        max_ele=arr[n-1]+1
        mini=0
        maxi=n-1
        min_ele=arr[0]
        for i in range(n):
            if i%2 ==0:
                arr[i]=arr[i]+(arr[maxi]%max_ele)*max_ele
                maxi-=1
            else:
                arr[i]=arr[i]+(arr[mini]%max_ele)*max_ele
                mini+=1
        for i in range(n):
            arr[i]=arr[i]//max_ele