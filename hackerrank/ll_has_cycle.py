"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    
    current = head
    seen = set()
    
    while current:
        key = hash(current)

        if key in seen:
            return True
        
        seen.add(key)
        
        current = current.next
    
    return False


    """
 s1Congrats, you solved this challenge!
 Test Case #0
 Test Case #1
    """