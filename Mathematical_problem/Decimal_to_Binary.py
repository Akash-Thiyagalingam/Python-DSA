# Decimal to Binary using recursion 
def ToBinary(num):
    if num == 0:
        return ""
    else :
        return ToBinary(num // 2) + str(num % 2)
    
print(ToBinary(233))

# Decimal to Binary without recursion
def Deci_to_binary(num):
    result=""
    while(num != 0):
        result = str(num % 2) + result
        num //= 2
    return result

print(Deci_to_binary(233))