# Find number steps to reach bottom left corner of the matrix grid
# Constraints : only you will one step down or one step rigth at the each step
def grid_path(n,m):
    # Where n is the number of rows and m is the number of coloums 
    if n == 1 or m == 1:
        # Here if only row or col is 1 there is one way to reach the Bottom left
        return 1
    else :
        return grid_path(n, m-1) + grid_path(n-1, m)

print(grid_path(3,4))
