#Implement a Queue using Stack
''' Functions   Time Complexity   Space Complexity
     Empty()         O(1)               O(1)
     push()          O(N)               O(N) 
     pop()           O(N)               O(N)
     peek()          O(1)               O(1)
     size()          O(N)               O(1)                                         
    '''
class Queue:
    def __init__(self):
        self.stack = []
        self.temp = []
        self.length = 0

    def push(self, x) :
        self.stack.append(x)
        self.length += 1

    def pop(self):
        while self.length > 1:
            self.temp.append(self.stack.pop())
            self.length -= 1
            
        res = self.stack.pop()
        self.length -= 1

        while self.temp:
            self.stack.append(self.temp.pop())
            self.length += 1
        return res

    def peek(self):
        return self.stack[0] if self.stack else -1

    def empty(self):
        return False if self.stack else True
