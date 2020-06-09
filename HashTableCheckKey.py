
"""
This class implementation is specifically focussing on updating a particular
value of  a specific key. The class has a method called setVal. This method
checks the particular hard coded index 10 of the hash table and loops through
that list to check if it contains the key. If it does, the specific index is
replaced with a new value other wise the new key value pair is appended to the
list in that index

"""


class HashTableAlgo:
  
  def __init__(self,size):
    self.size = size
    self.hashTableAttr = self.createHashTable()
    
  def createHashTable(self):
    return [[] for i in range(self.size)]
  
  def setVal(self,key,value):
    
    """
    This method looks for  specific key in a hard coded index which is 10.
    Then if the key is found, updates the original value with the new one
    Otherwise, if the key is not found it appends the new key value pair
    in the index 10 of the hash table sized 256
    """
    
    indexVal = 10                           # hard coded index in which key is being searched for
    bucket = self.hashTableAttr[indexVal]
    foundKey = False
    for index, record in enumerate(bucket):
      recordKey , recordVal = record
      if recordKey == key:
        foundKey = True
        break
    if foundKey == True:
      bucket[index] = (key, value)
    else:
      bucket.append((key,value))
    return self.hashTableAttr
      
  def __str__(self):
    return ''.join(str(item) for item in self.hashTableAttr)
  
hashTable = HashTableAlgo(250)
print(hashTable)

hashTable.setVal('sangavi@example.com','age is 23')
hashTable.setVal('saranya@example.com', 'age is 23')
print(hashTable)

hashTable.setVal('sangavi@example.com', 'loves coding')












