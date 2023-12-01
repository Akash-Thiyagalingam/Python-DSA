#Find the duplicate number in the range of 1 to n
def find_duplicate(arr): 
    slow = arr[0]
    fast = arr[0]
    fast = arr[fast]
    while(slow != fast) :
        slow = arr[slow]
        fast = arr[fast]
        fast = arr[fast]
    return arr[fast]

# By using the negative value
def duplicate(arr): 
    i = 0
    while True:
        try :
            if arr[abs(arr[i])] >= 0:
                arr[abs(arr[i])] = -arr[abs(arr[i])]
            else:
                return abs(arr[i])
        except :
            break
        i += 1
