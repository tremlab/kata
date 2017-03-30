""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

"""is this binary tree a SEARCH tree?"""


def check_binary_search_tree_(root):
    
    is_search = True
    
    def validate_node(node, max, min):
        
        if node == None:
            return True
        
        if node.data < max and node.data > min:
            return validate_node(node.left, node.data, min) and validate_node(node.right, max, node.data)    
        else:
            return False
    
    is_search = validate_node(root, float('inf'), -float('inf'))
  
    return is_search

    """Congrats, you solved this challenge!
 Test Case #0
 Test Case #1
 Test Case #2
 Test Case #3
 Test Case #4
 Test Case #5
 Test Case #6
 Test Case #7
 Test Case #8
 Test Case #9
 Test Case #10
 Test Case #11
 Test Case #12
 Test Case #13
    """