class Node:
  
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        
    def __str__(self):
        return f"{self.data}"
      
class Tree:
    
    def __init__(self):
        self.root = None
      
    def insert(self, value):
        if self.root == None:
            self.root = value
        else:
            self._insert(self.root, value)
    
    def _insert(self, node, value):
        if value.data < node.data:
            if node.left == None:
                node.left = value
            else:
                self._insert(node.left, value)
        else:
            if node.right == None:
                node.right = value
            else:
                self._insert(node.right, value)
                
    def search(self, node, value):
        if self.root != None:
            isFound = self._search(self.root, value)
            if isFound == True:
                return True
            else:
                return False
        else:
            return None
    
    def _search(self, node, value):
        if value.data < node.data and node.left != None:
            return self._search(node.left, value)
        elif value.data > node.data and node.right != None:
            return self._search(node.right, value)
        elif value.data == node.data:
            return True
        else:
            return False
          
    # printing the binary tree in INORDER
    def inorder(self):
        self._inorder(self.root)
    
    def _inorder(self, node):
       if node != None: # if this none is not given, recursion doesnt 
            self._inorder(node.left) #even if there is no left or right nodes
            print(node.data)
            self._inorder(node.right)




node8 = Node(8)
node9 = Node(9)
node1 = Node(1)
node2 = Node(2)
node11 = Node(11)
node13 = Node(13)

tree = Tree()
tree.insert(node8)
tree.insert(node9)
tree.insert(node1)
tree.insert(node2)

tree.root.data
tree.root.left.data
tree.root.left.right.data
tree.root.right.data

tree.search(tree.root, node13)
tree.inorder()