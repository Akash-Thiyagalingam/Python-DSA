def palin(s):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[-1]:
        return palin(s[1:-1])
    return False
    

def longestPalin(s):
    if len(s) == 0:
        return ""
    if palin(s) :
        return s
    left = longestPalin(s[1:])
    right = longestPalin(s[:-1])
    
    return (left if len(left) > len(right) else right)

print(longestPalin('skakasa'))