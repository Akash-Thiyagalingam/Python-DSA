#Implementing Queue using list
''' Functions   Time Complexity   Space Complexity
     isEmpty()         O(1)               O(1)
     enqueue()          O(1)               O(1) 
     dequeue()           O(1)               O(1)
     size()          O(1)               O(1)                                         
    '''
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
print(q.isEmpty())
print(q.enqueue(5))
print(q.enqueue(6))
print(q.enqueue(7))
print(q.size())
