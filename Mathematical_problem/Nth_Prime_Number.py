# Finding Nth prime Number
# Time Complexity: O(N)
# Space Complexity: O(k) 
#        where k is total number prime number in between n. 
def nth_prime(n):
    each_prime = 2
    prime_list = [2,3]
    length = 2
    while True :
        if (length == n):
            return prime_list[-1]
        else:
            for i in range(int(length**0.5)+1):
                if each_prime % prime_list[i] == 0:
                    break
            else:
                prime_list += [each_prime]
                length += 1
        each_prime += 1
                   
import time
st = time.time()
print(nth_prime(10001))
print(time.time()-st)

                    
