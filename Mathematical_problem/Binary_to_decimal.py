
# Binary to Decimal without recursion
def ToDecimal(Binary):
    num = 0
    digit = 0
    for i in Binary[::-1]:
        num += int(i)*(2**digit)
        digit += 1
    return num

print(ToDecimal("11101001"))

def Binary_to_decimal(Binary):
    if Binary == "0":
        return 0
    elif Binary == "1":
        return 1
    else:
        return (Binary_to_decimal(Binary[1:]))*2 
    
print(Binary_to_decimal("11101001"))