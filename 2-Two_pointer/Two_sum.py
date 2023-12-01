# To find the sum of pair of element in the sorted array that is equal to the target element
# Time Complexity: O(N)
# Space Complexity: O(1)

def twoSum(nums, target) :
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        if target > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum
    return [-1, -1]

print(twoSum([1,2,3,4,5,6,7],13))
