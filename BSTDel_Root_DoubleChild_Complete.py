

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
        Trying to delete a node with two chidren. It could be the root node of the tree,
        or it could be a sub tree with two children one on each side. There are two ways
        to go about it. Pick either left or right sub tree. Right is chosen here. Find the
        minimum number in the right subtree, and make it the root and delete the duplicate.
        Min is chosen because everything to the right of the root should be higher than the
        root. The minimum is found using a helper/private finction
        
        """
        self._delete(self.root, None, None, num)
        
        

    def _delete(self,current, previous, isLeft, num):            
        if current != None:               
            if current.data == num.data:
                if current.left != None and current.right != None:                
                    """
                    This portion is used to delete a node that could be the root node 
                    or could be a node that has two children. It calls a helper function
                    to perform the  rest
                    
                    """
                    minNode = self.minRightSub(current.right)                 # Pass the right child of the root. we work with right sub tree hence forth inside this conditiona
                    current.data = minNode.data                                   # PLace the minimum node in the current node, which is the root or the node with two children
                    self._delete(current.right, current, False, minNode)

                elif current.left == None and current.right == None:
                    if previous != None:
                        if isLeft:
                            previous.left = None                      # if there is only one node and that is root
                        else:                                         # There wouldnt be a previous node. None.left will throw an error
                            previous.right = None                     #Thats why we have previous.None check one conditional above
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
                
    def minRightSub(self, current):
        if current.left == None:                                          # If this node doesnt have a left child, it is the least in the right sub tree
            return current
        else:                                                             # Pass the left child as current, because we must check if the left node doesnt have a further left 
            return self.minRightSub(current.left)    # Recursively find the left element with no further left child

node8 = Node(8)
node9 = Node(9)
node1 = Node(1)
node2 = Node(2)
node11 = Node(11)
node13 = Node(13)
node0 = Node(0)

tree = Tree()
tree.insert(node8)
tree.insert(node9)
tree.insert(node1)
tree.insert(node2)
tree.insert(node11)
tree.insert(node0)

tree.root.data
tree.root.left.data
tree.root.left.right.data
tree.root.right.data

tree.search(tree.root, node11)
tree.inorder()

tree.delete(node0)
tree.inorder()

