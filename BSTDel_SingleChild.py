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
            
    def delete(self,num): 
        
        """
        This function deletes a node with one child.
        Whether it has a left child or right child is not known
        But the element is searched for recursively, along the
        left or right depending on the element it is compared
        with. Then if the child is in the left, and the current
        node is to the left, the left child is placed to the left
        of the parent node. and vice versa
        
        """
        self._delete(self.root, None, None, num)
        
        
            
    def _delete(self,current, previous, isLeft, num):            
        if current != None:
            if current.data == num.data:
                if current.left == None and current.right == None: # a node with no children
                    if previous != None:
                        if isLeft:
                            previous.left = None              # if there is only one node and that is root
                        else:                                 # There wouldnt be a previous node. None.left will throw an error
                            previous.right = None             # Thats why we have previous.None check one conditional above
                    else:
                        self.root = None
                elif current.left == None:
                    if previous != None:
                        if isLeft :
                            previous.left = current.right
                        else:
                            previous.right = current.right
                else:
                    if previous != None:
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
node13 = Node(13)

tree = Tree()
tree.insert(node8)
tree.insert(node9)
tree.insert(node1)
tree.insert(node2)
tree.insert(node11)

tree.root.data
tree.root.left.data
tree.root.left.right.data
tree.root.right.data

tree.search(tree.root, node11)
tree.inorder()
tree.delete(node11)
tree.inorder()

