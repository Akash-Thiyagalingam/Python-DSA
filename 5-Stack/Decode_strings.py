#Given an encoded string, return its decoded string.
#The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
#Note that k is guaranteed to be a positive integer.

"""Example 1:
        Input: s = "3[a]2[bc]"
        Output: "aaabcbc" """

#Time Complexity: O(N^2)
#Space Complexity: O(1)

def decodeString(s):
        stack=[]
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i]) # 1
            else:
                substr=''
                while stack and stack[-1]!= '[': 
                    substr=stack.pop() + substr
                
                stack.pop() 
                k =''
                while stack and stack[-1].isdigit(): 
                    k = stack.pop() + k
                
                stack.append( int(k) * substr  ) 
        
        return ''.join(stack)

print(decodeString("3[a]2[bc]"))
