"""Design a stack that supports push, pop, top, and retrieving the minimum
    element in constant time.
    Implement the MinStack class:
        MinStack() initializes the stack object.
        void push(int val) pushes the element val onto the stack.
        void pop() removes the element on the top of the stack.
        int top() gets the top element of the stack.
        int getMin() retrieves the minimum element in the stack."""

""" Functions   Time Complexity   Space Complexity
    isEmpty()        O(1)               O(1)
     push()          O(1)               O(1) 
     pop()           O(1)               O(1)
     peek()          O(1)               O(1)
     size()          O(N)               O(1)                                         
    """
class MinStack:
    def __init__(self):
        self.stack =[]
        self.minStack = []

    def push(self, val: int) -> None:
        self.Min = float('inf') if not self.stack else self.minStack[-1]
        self.Min = self.Min if self.Min < val else val
        self.stack.append(val)
        self.minStack.append(self.Min)

    def pop(self) -> None:
        if self.stack: 
            self.stack.pop()
            self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
