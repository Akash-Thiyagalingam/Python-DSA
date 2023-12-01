#Implementation of stack using queues.
""" Functions   Time Complexity   Space Complexity
     Empty()         O(1)               O(1)
     push()          O(N)               O(N) 
     pop()           O(N)               O(N)
     peek()          O(1)               O(1)
     size()          O(N)               O(1)                                         
    """

class Stack:
    def __init__(self):
        self.queue = deque()
        self.temp = deque()
        self.length = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.length += 1

    def pop(self) -> int:
        while self.length > 1:
            self.temp.append(self.queue.popleft())
            self.length -= 1

        res = self.queue.popleft()
        self.length -= 1

        while self.temp:
            self.queue.append(self.temp.popleft())
            self.length += 1
        return res

    def top(self) -> int:
        return self.queue[-1] if self.queue else -1

    def empty(self) -> bool:
        return True if not self.queue else False
    
s = Stack()
s.push(5)
s.push(10)
s.push(12)
print(s.empty())
print(s.top())
print(s.pop())
print(s.size())
