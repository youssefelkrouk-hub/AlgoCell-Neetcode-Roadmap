# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def __init__(self) :
        self.rs = -1
    def helper( self , root ) : 
        if not root : 
            return 0  
        curr = root.val 
        maxLeft = max( 0 , self.helper( root.left ) ) 
        maxRight = max( 0 , self.helper( root.right ) )
        self.rs = max( self.rs , curr + maxRight + maxLeft ) 
        return curr + max( maxLeft , maxRight ) 
    def maxPathSum(self, root):
        self.rs = root.val 
        self.helper( root ) 
        return self.rs 