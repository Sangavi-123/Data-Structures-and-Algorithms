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
            
    def delete(self, num):
        self._delete(self.root, None,None,num)
        
    def minRightSubtree(self, node):
        if node.left == None:
            return node
        else:
            return self.minRightSubtree(node.left)
    
    def _delete(self,current, previous, isLeft, num):
        if current != None:
            if num.data == current.data:
                if current.left != None and current.right != None:
                    # choose either left or right subtree, choosing right
                    # find the minuimum element in the right sub tree
                    minChild = self.minRightSubtree(current.right)
                    current.data = minChild.data
                    self._delete(current.right, current, False, minChild)
                    
                elif current.left == None and current.right == None:
                    if previous == None:   # There is only one node which is the root
                        self.root = None
                    else:
                        if isLeft == True:
                            previous.left = None
                        else:
                            previous.right = None
                
                elif current.left == None:  # Deleting nodes with one child in the right
                    if isLeft:
                        previous.left = current.right
                    else:
                        previous.right = current.right
                else: # implying the right child is not present, child is in the left
                    if isLeft:
                        previous.left = current.left
                    else:
                        previous.right = current.left
            elif num.data < current.data:
                self._delete(current.left, current, True, num)
            else:
                self._delete(current.right, current, False, num)
                  
                  
node8 = Node(8)
node9 = Node(9)
node1 = Node(1)
node2 = Node(2)
node11 = Node(11)

tree = Tree()
tree.insert(node8)
tree.insert(node9)
tree.insert(node1)
tree.insert(node2)
tree.insert(node11)
            

tree.inorder()
tree.root.data
tree.root.left.data
tree.root.left.right.data
tree.root.right.data
tree.root.right.right.data

tree.delete(node8)
tree.inorder()


