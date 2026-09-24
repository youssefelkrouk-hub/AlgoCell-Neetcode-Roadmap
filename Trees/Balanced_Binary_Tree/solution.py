# Definition for a binary tree node

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution(object):
    def isValid( self , root ) : 
        if not root : 
            return 0 
        a = self.isValid( root.left )  
        b= self.isValid( root.right ) 
        if a != -1 and b != -1 and abs( a - b ) <= 1 : 
            return max( a , b ) + 1 
        return -1 

    def isBalanced(self, root):
        if not root : 
            return True 
        if self.isValid( root ) != -1 :
            return True 
        return False 
        
        