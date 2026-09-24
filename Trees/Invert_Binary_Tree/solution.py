# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invert( self , root ) : 
        if not root : 
            return 
        temp = root.right 
        root.right = root.left 
        root.left = temp 
        self.invert( root.left )
        self.invert( root.right ) 
    def invertTree(self, root):
        self.invert( root )
        return root 
        