class Node:

# Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

# A binary search tree

class BinarySearchTree:

  # Constructor to create a new BST
    def __init__(self):
      self.root = None
#### my code:

    def findLargestSmallerKey(self, num):
      largest_value = 0
      current = self.root
    
    while current:
      val = current.key
      if num  <= val:
        current = current.left
      else:
        largest_value = current.key
        current = current.right
        
    return largest_value
