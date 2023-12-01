def anagram(str1,str2):
    str1=str1.replace(' ','').lower()
    str2=str2.replace(' ','').lower()
    return sorted(str1) == sorted(str2)

print(anagram('akash','ks haa'))



#Without using sorted method
def ana_gram (str1,str2):
    str1=str1.replace(' ','').lower()
    str2=str2.replace(' ','').lower()
    
    #Check the length of the strings
    if len(str1)!=len(str2):
        return False
    
    #Count the ferquency of character in str1
    count={}
    for i in str1:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1
    
    #Decrease the character in count
    for i in str2:
        if i in count:
            count[i]-=1
        else:
            count[i]=1
            
    #check letters in count
    for i in count:
        if count[i]!=0:
            return False
    return True

print(ana_gram('akash','ks haa'))
