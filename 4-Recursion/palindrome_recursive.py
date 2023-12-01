# Finding the given word is palindrome or not
def ispalindrome(word):
    if len(word) == 0 or len(word) == 1 :
        return True
    if word[0] == word[-1]:
        return ispalindrome(word[1:len(word)-1])
    # Here, this is recursive function so if the above condition is getting false
    # This return will execute
    return False 

