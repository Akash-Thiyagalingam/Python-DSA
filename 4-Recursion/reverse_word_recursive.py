#Reversing a word using Recursion
def reverse_word(word):
    if  word == "":
        return ""
    else:
        return reverse_word(word[1:len(word)])+word[0]

print(reverse_word('Hello world'))
    
