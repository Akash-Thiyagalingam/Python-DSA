# To convert Octal number to Decimal number
# Time Complexity: O(L), Where L is the length of digits
# Space Complexity: O(1)
def octToDec(n):
    pos = 0
    decimal = 0
    while(n != 0):
        rem = n % 10
        decimal += rem * pow(8, pos)
        n //= 10
        pos += 1
    return decimal

print(octToDec(200))




