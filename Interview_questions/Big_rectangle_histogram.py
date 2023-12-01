# To find the largest rectangle in histogram 
# The histogram is represented in an array 
# The program for this problem is given below
# Time complexity : O(n^2)
# Space complexity : O(1)
def max_rect(n):
    rect = 0
    for each in range(len(n)):
        count = 0
        for i in range(each, -1, -1):
            if n[i] >= n[each]:
                count += 1
            else: 
                break
        for i in range(each+1, len(n)):
            if n[i] >= n[each]:
                count += 1
            else: 
                break
        rect = (n[each] * count) if (n[each] * count) > rect else rect
    return rect


