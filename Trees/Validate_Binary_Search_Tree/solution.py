# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isValidBST(self, root):
        def dfs( root , a , b ) : 
            if not root : 
                return True 
            elif root.val <= a or root.val >= b : 
                return False 
            else : 
                return dfs( root.left , a , root.val ) and dfs( root.right , root.val , b )
        return dfs( root , -float('inf') , float('inf') )
        