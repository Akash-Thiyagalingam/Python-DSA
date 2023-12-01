#It is suitable for the 2D array which is completly sorted
#Time complexity : O(N)
def search_2D(arr,target):
    row=0
    col=len(arr[0])-1
    while(row<=col):
        if (arr[row][col] == target):
            return [row,col]
        elif (arr[row][col] > target):
            col-=1
        else:
            row+=1

print(search_2D([[1,2,3,4],[5,6,7,8],[9,10,11,12]],12))
