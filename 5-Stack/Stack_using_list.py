#Implementing stack using list.
""" Functions   Time Complexity   Space Complexity
    isEmpty()        O(1)               O(1)
     push()          O(1)               O(1) 
     pop()           O(1)               O(1)
     peek()          O(1)               O(1)
     size()          O(N)               O(1)                                         
    """

class Stack:
    #Initialization of stack object
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

s = Stack()
print(s.isEmpty())
s.push(5)
s.push(10)
s.push(12)
print(s.peek())
print(s.pop())
print(s.size())
