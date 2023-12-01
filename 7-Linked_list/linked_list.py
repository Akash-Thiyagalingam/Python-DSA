class Node:
  def __init__(self, value = None):
    self.value = value
    self.next = None

class Linkedlist:
  #This Initialization method takes any iterable input for creating a Linked list
  def __init__(self, obj):
    try:
      iter(obj)
      self.head = Node(next(obj))
    except StopIteration:
      print("NoInputReceived")
    else:
      self.length = 1
      temp = self.head
      while True:
        try:
          temp.next = Node(next(obj))
        except StopIteration:
          break
        self.length += 1
        temp = temp.next

  # We can use this magic method to print the elements 
  # By using print() finction with the object name as a parameter
  def __str__(self) -> str: 
    str_list = ""           
    curr = self.head
    while curr :
      str_list += str(curr.value) + (", " if curr.next != None else "")
      curr = curr.next
    return "[" + str_list + "]"

  #Method for Printing the linked list
  def printList(self):
    temp = self.head
    while temp:
      print(temp.value, end = " ")
      temp = temp.next

  #Method for sum of values of the nodes in the linked list
  def sum(self):
    temp = self.head
    while temp:
      sum += temp.value
      temp = temp.next
    return sum

  #Method for Insert at any place in the linked list
  def insertAt(self,val,pos=1):
    temp = self.head
    if pos == 1:
      flag = temp
      temp = Node(val)
      temp.next = flag
      self.head = temp
    else:
      for node in range(pos-1):
        if node == pos-2:
          continue
        temp = temp.next
      flag = temp.next
      temp.next = Node(val)
      temp.next.next = flag

  #Method for reversing Linked list
  def reverseList(self):
    cur = self.head
    prev = None
    while cur:
      next = cur.next
      cur.next = prev
      prev = cur
      cur = next
    self.head = prev

  #Method for search an element in a linked list
  def SearchElement(self, ele):
    temp = self.head
    idx = 0
    while temp:
      if ele == temp.value:
        return idx
      temp = temp.next
      idx += 1
    return idx

  #Method for deleting the first node
  def deleteAtBegin(self):
    try:
      self.head = self.head.next
    except:
      print("Linked list already empty")

  #Method for deleting the last node
  def deleteAtEnd(self):
    temp = self.head
    while temp.next:
      temp = temp.next
    temp = None

  #Method for deleting the node at given index
  def deleteAt(self, index):
    temp = self.head
    for idx in range(1, index):
      temp = temp.next
    temp.next = temp.next.next

  #Method for finding value of middle node
  def middle(self):
    slow = self.head
    try:
      fast = self.head.next
    except:
      return self.head.value
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    return slow.value

  #Method for counting occurences of each value of node in linked list
  def countValues(self):
    count = {}
    temp = self.head
    while temp and temp.next:
      if temp.value not in count:
        count[temp.value] = 1
      else:
        count[temp.value] += 1
      temp = temp.next
    return count

  #Method for removing nodes which has repeated values in the linked list
  def removeRepeated(self):
    Set = set()
    temp= self.head
    Set.add(temp.value)

    while temp and temp.next and temp.next.next:
      if temp.next.value not in Set:
        Set.add(temp.next.value)
        temp = temp.next
      else:
        temp.next = temp.next.next

  #Method for deducting, if there is loop present or not in linked list
  def detectLoop(self):
    slow = self.head
    fast = self.head
    while(slow and fast and fast.next):
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True
      return False

    
        

if __name__ == "__main__":
  linked_list = Linkedlist(map(int, input().split()))
  print(linked_list)
  linked_list.printList()
  linked_list.insertAt(5,2)
  linked_list.printList()
  linked_list.reverseList()
  linked_list.printList()
  linked_list.SearchElement(16)
  linked_list.deleteAtBegin()
  linked_list.printList()
  linked_list.deleteAtEnd()
  linked_list.printList()
  linked_list.deleteAt(3)
  linked_list.printList()
  linked_list.middle()
  linked_list.countValues()
  linked_list.removeRepeated()
  linked_list.printList()
  linked_list.detectLoop()