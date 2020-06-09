"""

This implementation is the continuation of the code, HashTableCheckKey.py. 
Here there is a new method called the getVal, which does a linear search to
find if a key is present and retrieves the value.

"""

class HashTableAlgo:
  
  def __init__(self, size):
    self.size = size
    self.hashTableAttr = self.createHashTable()
    
  def createHashTable(self):
    return [[] for item in range(self.size)]
  
  def setVal(self, key, value):
    indexVal = hash(key) % self.size 
    bucket = self.hashTableAttr[indexVal]
    
    foundKey = False
    for index, record in enumerate(bucket):
      recordKey, recordVal = record
      if recordKey == key:
        foundKey = True
        break
    if foundKey:
      bucket[index] = (key,value)
    else:
      bucket.append((key,value))
    
    return self.hashTableAttr
  
  def getVal(self, key):
    indexVal = hash(key) % self.size
    bucket = self.hashTableAttr[indexVal]
    
    for item in bucket:
      recordKey, recordValue = item
      if recordKey == key:
        return recordValue
        break
    return recordValue
  
  def delValue(self, key):
    indVal = hash(key) % self.size
    bucket = self.hashTableAttr[indVal]
    
    for index, record in enumerate(bucket):
      recordKey, recordVal = record
      if recordKey == key:
        return bucket.pop(index)
    
  def __str__(self):
    return ''.join(str(item) for item in self.hashTableAttr)

hashTable = HashTableAlgo(256)
print(hashTable)    

hashTable.setVal('sangavi@example.com', 'age is 23')
print(hashTable)

hashTable.setVal('saranya@example.com', 'age is 23')
print(hashTable)

hashTable.setVal('sangavi@example.com', 'loves coding')
print(hashTable)

hashTable.setVal('gopinath@example.com', 'Great Human')
print(hashTable)

print(hashTable.delValue('gopinath@example.com'))

    