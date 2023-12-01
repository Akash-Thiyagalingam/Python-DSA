# Find the Index of the First Occurrence of needle(string) in a haystack(string) 
# Time Complexity: O(N)
# Space Complexity: O(1)

def strStr(self, haystack, needle):
        start = 0
        end = len(needle)      
        max_size = len(haystack)

        while end <= max_size:
            if haystack[start:end] == needle:
                return start
            start += 1
            end += 1

        if haystack == needle:
            return max_size-1

        return -1

print(strStr("itlookseasybutnoteasy","easy"))