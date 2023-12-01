def Sum(a,b):
    return a+b
def sum(*arg):
    tot = 0
    for i in arg:
        tot += i
    return tot

print(Sum(1,2))
print(type((1,)))

from abc import ABC , abstractmethod
class parent(ABC):
    @abstractmethod
    def method(myself):
        pass

class child(parent):
    def method(myself):
        pass

print(issubclass(child, parent))
