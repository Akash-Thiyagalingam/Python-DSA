# Binary Search 
# It is searching an element in the sorted array or list
# Time Complexity : O(log N)
# Space Complexity : O(1)
from jovian.pythondsa import evaluate_test_cases #evaluate_test_case used for evaluate single test case 
import Test_cases_for_binary_search              #for multiple testcases use evaluate_test_cases
def Binary_search(arr,target):          
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if (arr[mid]==target):
            return mid
        elif(arr[mid] > target):
            high=mid-1
        else:
            low=mid+1
    return -1

#Attempting testcases by ourselves
for test in Test_cases_for_binary_search.testcases:
    print(Binary_search(**test["input"]) == test["output"])
   
#Attempting testcases by jovian libraty
evaluate_test_cases(Binary_search,Test_cases_for_binary_search.testcases)
