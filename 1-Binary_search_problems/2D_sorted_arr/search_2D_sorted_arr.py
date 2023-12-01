""""Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row."""

# Search a element in completly sorted 2D array Using Binary search 
# Time complexity : O(2logn) => O(logn)
def row_search(matrix, row, target):  
    low=0
    high=len(matrix)-1  
    while((high-low)>=0):
        mid=(high+low)//2
        if (matrix[row][mid] == target):
            return ([row,mid])
        elif(target<matrix[row][mid]):
            high=mid-1
        elif(target>matrix[row][mid]):
            low=mid+1
    return -1

def col_search(matrix, col, target):  #To find ceiling of a target 
    low=0                          #Because the last in a row
    high=len(matrix[0])-1             #lessthan the first element in a coloumn
    while((high-low)>=0):
        mid=(high+low)//2
        if (target==matrix[mid][col]):
            return mid
        elif(target<matrix[mid][col]):
            high=mid-1
        elif(target>matrix[mid][col]):
            low=mid+1
    return high


def find_element(matrix,target):
    if len(matrix)==0:
        return -1
    row=col_search(matrix, 0, target)
    return row_search(matrix, row, target)


print(find_element([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],14))