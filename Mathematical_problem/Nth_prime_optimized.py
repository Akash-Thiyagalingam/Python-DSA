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

#Time complexity : O(sqrt(m))
# Space complexity : O(m)
