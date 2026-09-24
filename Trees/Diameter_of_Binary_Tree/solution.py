# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__( self ) :
        self.rs = 0 
    def getHeight( self , root ) :
        if not root : 
            return 0 
        l = self.getHeight( root.left )
        r = self.getHeight( root.right )
        self.rs = max( self.rs , l + r )
        return max( l , r ) + 1
    def diameterOfBinaryTree(self, root):
        self.getHeight( root ) 
        return self.rs