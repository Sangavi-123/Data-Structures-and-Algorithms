

class Node():
  
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f"{self.data}"
      
class LinkedList:
  
    def __init__(self):
        self.head = None
        self.tail = None
      
    def addVal(self,newest):
        if self.head == None:
            self.head = newest
            self.tail = newest
        else:
            self.tail.next = newest
            self.tail = newest
    
    def printList(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode)
            currentNode = currentNode.next
    
    def addFromHead(self, newest):
        head = self.head
        headNext = self.head.next
        self.head = newest
        self.head.next = head
        print(self.head, self.head.next)
        
    def addFromLast(self,newest):
        last = self.tail
        self.tail = newest
        last.next = self.tail 
        print(last.next, self.tail)
      
    def searchByVal(self,element):
        "Searches for a particular node and returns it's index if found"
        current = self.head
        count = -1
        
        while current != None:
            count += 1 
            if element == current:
              print(f"The element was found at index {count}")
            current = current.next
    def length(self):
        current = self.head
        count = 0
        
        while current != None:
          count += 1
          current = current.next
        return f"The length of the list is {count}"
    
    def recursiveRevLinkedList(self,current, previous):
        if self.head == None:
            return
        elif current.next == None:
            self.tail = self.head
            current.next = previous
            self.head = current
        else:
            next = current.next
            current.next = previous
            self.recursiveRevLinkedList(next, current)
      
          
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

linkedList = LinkedList()
linkedList.addVal(node1)
linkedList.addVal(node2)
linkedList.addVal(node3)
linkedList.addVal(node4)
linkedList.addVal(node5) 

linkedList.printList()
linkedList.addFromHead(node6)
linkedList.addFromLast(node7)
linkedList.searchByVal(node7)

linkedList.length()
print(linkedList.recursiveRevLinkedList(linkedList.head,None))
      