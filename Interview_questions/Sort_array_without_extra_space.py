# Sort two arrays without extra space
# Time complexity : O(NlogN) 
# Space complexity : O(1)
def merge(self,arr1,arr2,n,m):
        gap = (n + m) //2
        while (gap != 0):
            first = 0
            last = gap
            while (last < (n+m)):
                if (first < n) and (last < n):
                    if arr1[first] > arr1[last]:
                        arr1[first], arr1[last] = arr1[last], arr1[first]
                elif (first < n) and (last >= n):
                    if arr1[first] > arr2[last-n]:
                        arr1[first], arr2[last-n] = arr2[last-n], arr1[first]
                else:
                    if arr2[first-n] > arr2[last-n]:
                        arr2[first-n], arr2[last-n] = arr2[last-n], arr2[first-n]
                first += 1
                last += 1
            gap = gap//2