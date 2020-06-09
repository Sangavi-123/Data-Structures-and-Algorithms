"""
This code contains the implementation of queues
"""

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f"{self.data}"
      
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

print(node5)
      
class Queue:
  
    def __init__(self):
        self.head = None
        self.tail = None
        
    def addVal(self, x):
        if self.head == None:
            self.head = x
            self.tail = x
        else:
            self.tail.next = x
            self.tail = x
            
    def printQueue(self):
        current = self.head
        while current != None:
            print(f"{current}")
            current = current.next
            
    def pop(self):
        next = self.head.next
        self.head.next = None
        self.head = next
        
    def peek(self):
        "Check what the head of the queue poitns to"
        if self.head != None: return f"{self.head}"
        else: return f"The head point to none"
            
    def isEmpty(self):
        "Checks if the head is empty"
        if self.head == None:
          return f"The queue is empty"
        else:
          return f"The string contains data"
queue = Queue()
queue.addVal(node1)
queue.addVal(node2)
queue.addVal(node3)
queue.addVal(node4)
queue.addVal(node5)

queue.printQueue()
queue.pop()
queue.peek()
queue.isEmpty()
          
          