# To Remove the duplicates in sorted array
# Time Complexity: O(N)
# Space Complexity: O(1)

def removeDuplicates(nums, val) :
    curr_index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[curr_index] = nums[i]
            curr_index += 1
    return curr_index

print(removeDuplicates([2,4,5,6,7,11,23],23))
