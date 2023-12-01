def decor(fun):
    def wrapper(val):
        return fun(val) +10
    return wrapper   # Note here we are not using brackets.

@decor
def Sum(a):
    print("At initial 10")
    return a

#Creating a decatator function with unknown datatype with unkown number of arguments
def decorator(fun):
    def wrapper(*args, **kwargs):
        return fun(*args, **kwargs) +10
    return wrapper   # Note here we are not using brackets.

@decorator
def threeSum(a,b,c):
    print(f"At initial {a+b+c}")
    return a+b+c

print(threeSum(10,10,10))
