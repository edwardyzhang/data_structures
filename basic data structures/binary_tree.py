#Building a implementation of a binary tree

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    
        
"""
Creating a simple binary search tree of 

             50
           /    \
         30      70
        /  \    /  \
       10  45  60  100

"""

tree = BinaryTree
tree.root = Node(50)
tree.root.left = Node(30)
tree.root.right = Node(70)
tree.root.right.left = Node(60)
tree.root.left.left = Node(10)
tree.root.left.right = Node(45)
tree.root.right.right = Node(100)

