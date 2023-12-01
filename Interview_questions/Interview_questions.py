#Total number of swap to reverse a number
def no_of_it_to_rev(): 
    n=int(input("Enter the number: "))
    print("Number of moves: ", (((n-1)*((n-1)+1))//2)+1)

#Sorting user inputs and return middle
def User_sort(): 
    i=0
    arr=[]
    while(True):
        element=int(input())
        if element in arr:
            continue
        arr.append(element)
        if len(arr)==9:
            break

    for i in range (8):
        for j in range(i+1,9):
            if arr[i]>arr[j]:
                arr[i]=arr[i]+arr[j]
                arr[j]=arr[i]-arr[j]
                arr[i]=arr[i]-arr[j]