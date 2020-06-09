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

class Stack:
  
    def __init__(self):
        self.stackPointer = None
        
    def addVal(self, new):
        if self.stackPointer == None:
            self.stackPointer = new
        else:
            new.next = self.stackPointer
            self.stackPointer = new
          
    def printStack(self):
        current = self.stackPointer
        while current != None:
            print(f"{current}")
            current = current.next
            
    def pop(self):
        popped = self.stackPointer  
        next = self.stackPointer.next
        self.stackPointer = next
        return popped
      
    def peek(self):
        "find what is there in the stackPointer"
        return f"{self.stackPointer}"     
    
    def isEmpty(self):
        if self.stackPointer == None:
            return f"StackPointer is empty"
        else:
            return f"StackPointer conatins {self.stackPointer}"
                
stack = Stack()
stack.addVal(node1)
stack.addVal(node2)
stack.addVal(node3)
stack.addVal(node4)
stack.addVal(node5)

stack.printStack()
stack.pop()
stack.peek()
stack.isEmpty()